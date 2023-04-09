from collections import deque;
import sys

input = sys.stdin.readline;

def bfs():
    move = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]];
    while queue:
        
        tH, tX, tY = queue.popleft();

        for mH, mX, mY in move:
            h, x, y = tH+mH, tX+mX, tY+mY;

            #범위 벗어나는지 확인.
            # if (0<=h<H and 0<=x<N and 0<=y<M) == False: continue;
            if h < 0 or h >= H or x < 0 or x >= N or y < 0 or y >= M: continue;

            if tomato[h][x][y] == 0:
                tomato[h][x][y] = tomato[tH][tX][tY]+1;
                queue.append([h,x,y]);

M, N, H = list(map(int, input().split()));
tomato = [ [ list(map(int, input().split())) for _ in range(N) ] for _ in range(H) ];
# visit = [[ [0]*M for _ in range(N) ] for _ in range(H) ]
queue = deque([]);

for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j] == 1: 
                queue.append([h,i,j]);

#함수로 빼니까 속도가 훨씬 줄어듦 ㄷㄷ;;;;;
bfs();

result = 0;
for h in tomato:
    for n in h:
        for m in n:
            if m == 0: 
                print(-1);
                exit(0);
                
        result = max(result, max(n));

print(result-1);