import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split());
C, H = [], [];

for i in range(N):
    bList = list(map(int,input().split()));

    for j in range(N):
        if bList[j] == 1:
            H.append((i,j));
        elif bList[j] == 2:
            C.append((i,j));

min_dist = 10**30;

for x in combinations(C, M):
    city_dist = 0
    for h in H:
        city_dist += min([abs(h[0]-k[0])+abs(h[1]-k[1]) for k in x]);

    min_dist = min(min_dist, city_dist);

print(min_dist);

# https://aigong.tistory.com/467 백트래킹으로 품. 이해안감 ㅠㅠ
