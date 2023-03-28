#너비 그 자체 문제
# -1인지 체크하는게 추가로 필요.

from collections import deque;

def bfs (tqueue):

    while tqueue:

        for _ in range(len(tqueue)):
            y, x = tqueue.popleft();

            moveList = [(1, 0), (-1, 0), (0, 1), (0, -1)];
            for y1, x1 in moveList:
                my, mx = (y+y1, x+x1);
                
                #행렬범위를 벗어나면 건너뜀
                if 0 > my or my >= N: continue;
                if 0 > mx or mx >= M: continue;

                # 이미 방문했거나 -1이면 건너뜀
                if tBox[my][mx] != 0: continue;

                tBox[my][mx] = tBox[y][x] + 1;
                tqueue.append((my, mx));         

M, N = map(int, input().split(" "));
tqueue = deque([]);
check = [];

#M*N 행렬 만들기
tBox = [];
isAllRiped = True;
day = 0;

for i in range(N):
    tList = list(map(int, input().split(" ")));
    for idx, value in enumerate(tList):
        if value == 1:
            tqueue.append((i, idx)); #우선 찾아갈 위치 큐에 넣음.
        if value == 0:
            isAllRiped = False;
    tBox.append(tList);

if isAllRiped: print(0);
else :
    bfs(tqueue);

    for row in tBox:
        for tomato in row:
            if tomato == 0:
                print(-1);
                exit(0);
        day = max(day, max(row));

    print(day-1);