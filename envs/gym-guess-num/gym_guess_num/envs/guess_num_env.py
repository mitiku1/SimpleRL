import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_guess_num.spaces import NumGenSpace
import numpy as np


class GuessNumEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, num_digits = 4, repeat_digits=False):
        self.num_digits = num_digits
        self.repeat_digits = repeat_digits
        self.current_digits = None
    def step(self, action):
        assert type(action) == np.ndarray, "The action should be ndarray"
        assert self.current_digits is not None, "The reset method should be called before using this method"
        assert action.shape==(self.num_digits,), "The size of action is not compatible, expected ndarray of shape ({}, ) but got {} ".format(self.num_digits, action.shape)
        assert self.num_gen_space.contains(action), "This action:{} is not in the action space".format(action)
        if not self.repeat_digits:
            pass
        else:
            pass
    def reset(self):
        self.num_gen_space = NumGenSpace(self.num_digits, self.repeat_digits)
        self.current_digits = self.num_gen_space.sample()
        self.done = None
        
    def render(self, mode='human'):
        print("Current digits:", self.current_digits.tolist())
    def close(self):
        pass
    