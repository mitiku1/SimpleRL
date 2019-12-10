from models import StateModel
import gym_guess_num
import gym
import torch
from utils import ReplayMemory
from utils import Transition

def main():
    num_digits = 4
    state_size = 128
    embedding_dim = 8

    model = StateModel(num_digits, state_size, embedding_dim)
    
    env = gym.make("GuessNumEnv-v0")
    
    episodes = 100
    max_epside_len = 100

    replay_memory = ReplayMemory(1000)

    for ep in range(episodes):
        state, reward, done = env.reset()

        state = torch.from_numpy(state)
        action = torch.argmax(model((state[:, :-2].unsqueeze(0).long(), state[:, -2:].unsqueeze(0).float())), dim=-1) + 1 # Plus one because the action is composed of the numbers between 1 and 9
        
        next_state, reward, done = env.step(action.numpy().reshape(-1,))
        t = Transition(state=state, next_state=next_state, reward=reward, action=action)
        env.render()
        print(reward, done)
        break



if __name__ == "__main__":
    main()