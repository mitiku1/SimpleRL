import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_guess_num.spaces import NumGenSpace
import numpy as np
from gym_guess_num.datastructures import CustomQueue
import copy

class GuessNumEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, num_digits = 4, repeat_digits=False,observable_size = 128):
        self.num_digits = num_digits
        self.repeat_digits = repeat_digits
        self.current_digits = None
        self.observable_size = observable_size
        self.observed = None
        super(GuessNumEnv, self).__init__()
        
    def step(self, action):
        assert type(action) == np.ndarray, "The action should be ndarray"
        assert self.current_digits is not None, "The reset method should be called before using this method"
        assert action.shape==(self.num_digits,), "The size of action is not compatible, expected ndarray of shape ({}, ) but got {} ".format(self.num_digits, action.shape)
        assert self.num_gen_space.contains(action, repeating=True), "This action:{} is not in the action space".format(action)
        
        unique_nums = np.unique(action)
        
        digits_observation = 0 # Number of correctly guessed digits
        order_observation = 0 # Number of correctly guessed positions
        if unique_nums.shape == action.shape:
            for i in range(len(unique_nums)):
                if unique_nums[i]==self.current_digits[i]:
                    order_observation += 1
                if unique_nums[i] in self.current_digits:
                    digits_observation += 1
        else:
            for i in range(len(unique_nums)):
                if unique_nums[i] in self.current_digits:
                    digits_observation += 1
            for i in range(len(action)):
                if action[i] == self.current_digits[i]:
                    order_observation += 1
    
        observation = np.array(action.tolist()+[digits_observation, order_observation])
        self.observed.push(observation)
        
        reward, self.done = self.calculate_reward(digits_observation, order_observation)
        return copy.deepcopy(self.observed.to_numpy_array()), reward, self.done
                
    def reset(self):
        self.num_gen_space = NumGenSpace(self.num_digits, self.repeat_digits)
        self.current_digits = self.num_gen_space.sample()
        self.done = False
        self.observed = CustomQueue(self.num_digits + 2,  self.observable_size)
        
        return copy.deepcopy(self.observed.to_numpy_array()), 0, self.done
        
    def render(self, mode='human'):
        print("Current digits:", self.current_digits.tolist())
    def close(self):
        pass
    def calculate_reward(self, digits_observation, order_observation):
        if digits_observation== self.num_digits and order_observation == self.num_digits:
            reward = 100
            done = True
        else:
            reward = -(self.num_digits - digits_observation) - (self.num_digits - order_observation)
            done = False
        return reward, done
    