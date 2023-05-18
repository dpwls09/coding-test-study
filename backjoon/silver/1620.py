import sys
input = sys.stdin.readline;

N, M = map(int, input().strip().split());
nameKey = {};

for i in range(1, N+1):
    i = str(i);
    name = input().strip();
    nameKey[i] = name;
    nameKey[name] = i;

for _ in range(M):
    q = input().strip();
    print(nameKey[q]);