import gym
from gym import error, spaces, utils
import numpy as np

class NumGenSpace(spaces.space.Space):
    def __init__(self, num_digits, repeat_digits):
        self.num_digits = num_digits
        self.repeat_digits = repeat_digits
        super(NumGenSpace, self).__init__((num_digits, ), np.uint8)
    def sample(self):
        return self.__sample()
    def contains(self, x):
        if x.shape==(self.num_digits,):
            if self.repeat_digits:
                for digit in x:
                    if digit>9 or digit <= 0:
                        return False
                return True
            else:
                unique = np.unique(x)
                if unique.shape!=x.shape:
                    return False
                else:
                    for digit in x:
                        if digit>9 or digit <= 0:
                            return False
                    return True 
        return False
    def __sample(self):
        return np.random.randint(1, 10, size=(self.num_digits,), replace=self.repeat_digits)