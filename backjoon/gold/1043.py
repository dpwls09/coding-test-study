import sys
from collections import deque;

input = sys.stdin.readline;

N, M = map(int, input().strip().split());
Tcount, *Tmember = map(int, input().strip().split());
members = [[] for _ in range(N+1)]

party = []

for i in range(M):
    Pcount, *Pmember = map(int, input().strip().split());
    party.append(Pmember);

    for m in Pmember:
        members[m].append(i);

if Tcount == 0: 
    print(M)
    exit(0);

Tmember = deque(Tmember);

while Tmember:
    m = Tmember.pop();
    for p_idx in members[m]:
        for m in party[p_idx]:
            Tmember.append(m)
        party[p_idx] = [];


for p in party:
    if len(p)==0:
        M -= 1;
print(M);