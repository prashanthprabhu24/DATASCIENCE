import torch
from gptmodel import GPTLanguageModel
from transformer import Block
from datasetreading import get_data

inp = 'priya is angel '  # put any letters or words or statements


block_size = 256
n_embd = 384
n_head = 6
n_layer = 6

encode, decode, train_data, val_data, vocab_size = get_data()

device = 'cuda' if torch.cuda.is_available() else 'cpu'

c = torch.tensor([encode(inp)], dtype=torch.long, device=device)
print('Input Text : ', inp)

model = GPTLanguageModel()

print()
print('Output Text : ', )
l = torch.load('model1.pth', map_location=torch.device('cpu'))
print(decode(l.generate(c, max_new_tokens=500)[0].tolist()))
