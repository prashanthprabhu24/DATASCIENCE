import torch
import torch.nn as nn
from torch.nn import functional as F
import time
from datasetreading import get_data, get_batch

from gptmodel import GPTLanguageModel

batch_size = 64
block_size = 256
max_iters = 1
eval_interval = 500
learning_rate = 3e-4
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200
n_embd = 384
n_head = 6
n_layer = 6
dropout = 0.2

torch.manual_seed(1337)

encode, decode, train_data, val_data, vocab_size = get_data()


@torch.no_grad()
def estimate_loss():
    out = {}
    model.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X, Y = get_batch(split, train_data, val_data, block_size, batch_size, device)
            logits, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out


model = GPTLanguageModel()
m = model.to(device)

print(sum(p.numel() for p in m.parameters()) / 1e6, 'million parameters')

optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

for iter in range(max_iters):

    if iter % eval_interval == 0 or iter == max_iters - 1:
        losses = estimate_loss()
        print(f"step {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}")

    xb, yb = get_batch('train', train_data, val_data, block_size, batch_size, device)

    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

context = torch.zeros((1, 1), dtype=torch.long, device=device)
print(decode(m.generate(context, max_new_tokens=500)[0].tolist()))
t = time.asctime().split()
filename = 'output' + t[-1] + t[3] + t[4] + '.txt'
modelname = 'model' + t[-1] + t[3] + t[4] + '.pth'
open(filename, 'w').write(decode(m.generate(context, max_new_tokens=10000)[0].tolist()))
torch.save(m, modelname)
