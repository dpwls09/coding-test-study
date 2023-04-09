from itertools import combinations;
from collections import deque;
import copy;

def bfs (comb, room, queue): #visit를 매번 리셋해야하니까.
    move = [(1,0),(-1,0), (0,1), (0,-1)];

    for x,y in comb: 
        room[x][y] = 1;

    while queue:
        covX, covY = queue.popleft();
        for mX, mY in move:
            x, y = covX+mX, covY+mY;
            
            if 0 <= x < N and 0 <= y < M:

                if room[x][y] == 0:
                    room[x][y] = 2;
                    queue.append((x, y));
    
    return room;

def checkEmpty(room):
    count = 0;
    for row in room:
        for c in row:
            if c == 0: count += 1;
    
    return count;

N, M =  map(int, input().split());
room = [ list(map(int, input().split())) for _ in range(N)];

queue = [];
empty = [];
area = 0;

for i in range(N):
    for j in range(M):
        # if num == 1:
        if room[i][j] == 0:
            empty.append((i, j));
        elif room[i][j] == 2:
            queue.append((i, j));

#벽을 세울 수 있는 모든 조합을 구함.
for comb in list(combinations(empty, 3)):
    area = max(area, checkEmpty(bfs(comb, copy.deepcopy(room), deque(queue))));

print(area);