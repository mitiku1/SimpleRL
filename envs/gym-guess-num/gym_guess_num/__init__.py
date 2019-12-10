from gym.envs.registration import register
from gym_guess_num.envs import GuessNumEnv,GuessNumExtraHardEnv
register(
    id='GuessNumEnv-v0',
    entry_point='gym_guess_num.envs:GuessNumEnv',
    kwargs = dict(num_digits = 4, repeat_digits=False, observable_size = 128)
)
