import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_guess_num.spaces import NumGenSpace
import numpy as np
from gym_guess_num.datastructures import CustomQueue
import copy

class GuessNumExtraHardEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, num_digits = 4, repeat_digits=False,observable_size = 128):
        self.num_digits = num_digits
        self.repeat_digits = repeat_digits
        self.current_digits = None
        self.obserable_size = observable_size
        self.observed = None
        super(GuessNumExtraHardEnv, self).__init__()
        
    def step(self, action):
       pass
    def reset(self):
        pass
    def render(self, mode='human'):
        pass
    def close(self):
        pass
   
    