import torch
from torch import nn

class StateModel(nn.Module):
    def __init__(self, num_digits, state_size, embed_dim):
        super(StateModel, self).__init__()
        self.state_size = state_size
        self.embed_dim = embed_dim
        self.num_digits = num_digits
        self.embed = nn.Embedding(10, self.embed_dim)
        self.fc_o1 = nn.Linear(2, self.embed_dim)

        self.fc1 = nn.Linear(self.state_size * (self.num_digits + 1) * self.embed_dim, 64)
        self.fc2 = nn.Linear(64, 128)
        self.fc3 = nn.Linear(128, self.num_digits * 9)
        
    def forward(self, inputs):
        guess, obs = inputs
        guess_BS = guess.shape[0]
        obs_BS = obs.shape[0]
        assert guess_BS == obs_BS,"Batch size is incompitable" 
        g_emb = self.embed(guess)
        
        g_emb_BS = g_emb.shape[0]
        assert g_emb_BS == guess_BS, "Batch size has changed"
       
        obs_fc1 = self.fc_o1(obs)
        obs_fc1 =  obs_fc1.unsqueeze(2)
        cat_1 = torch.cat([g_emb, obs_fc1], dim=2)
        new_channels = self.state_size * (self.num_digits + 1) * self.embed_dim
        x = cat_1.view(-1, new_channels)
        x_bath_size = x.shape[0]
        assert x_bath_size==guess_BS, "Batch size has changed"

        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        x = x.view(-1, self.num_digits, 9)

        return x

