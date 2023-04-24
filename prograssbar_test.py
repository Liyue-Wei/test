import time
from tqdm import tqdm, trange

for i in trange(50):
    time.sleep(0.05)

for i in tqdm(range(100), desc='Processing'):
    time.sleep(0.05)

dic = ['a', 'b', 'c', 'd', 'e', 'f']
pbar = tqdm(dic)
for i in pbar:
    pbar.set_description('Processing '+i)
    time.sleep(0.2)