#그리디
from collections import deque;
import sys;

input = sys.stdin.readline;

N, K = map(int, input().strip().split());
unit = deque([]);

for _ in range(N):
    unit.append(int(input().strip()));

count = 0;

while K != 0:
    coin = unit.pop();
    
    if K < coin: continue;

    count += K // coin;
    K %= coin;

print(count);