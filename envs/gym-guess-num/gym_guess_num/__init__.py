from gym.envs.registration import register

register(
    id='guess-num-v0',
    entry_point='gym_guess_num.envs:GuessNumEnv',
)
register(
    id='guess-num-extrahard-v0',
    entry_point='gym_guess_num.envs:GuessNumExtraHardEnv',
)