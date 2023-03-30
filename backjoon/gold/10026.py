# from collections import deque;

# def bfs(kind=3):
    
#     visit = [[False]*N for _ in range(N)];

#     #이어서 탐색할 queue
#     queue = deque([]);
#     #스타트 지점 queue
#     startQ = deque([(0, 0)]);
#     #a-색약X b-색약O
#     current = "";
#     compareL = [(1, 0), (-1, 0), (0, 1), (0, -1)];
#     count = 1;

#     while startQ:
#         startX, startY = startQ.popleft();
        
#         if visit[startX][startY]: continue;

#         current = colors[startX][startY];
#         queue.append((startX, startY));
#         visit[startX][startY] = True;

#         while queue:
#             x, y = queue.popleft();
#             for x1, y1 in compareL:
#                 mx, my = x1+x, y1+y;
            
#                 if mx < 0 or mx >= N: continue;
#                 if my < 0 or my >= N: continue;

#                 compare = colors[mx][my];
#                 if visit[mx][my]: continue;

#                 if current == compare or (kind == 2 and current != "B" and compare != "B"):
#                     queue.append((mx, my));
#                     visit[mx][my] = True;
#                     continue;

#                 startQ.append((mx, my));
#                 continue;
            
#         count += 1;
#     return count;

# N = int(input());

# colors = [ list(input()) for _ in range(N)];

# a = bfs();
# b = bfs(2);


# print(a, b);


from collections import deque;

def bfs(i, j, kind=3):
    
    #이어서 탐색할 queue
    queue = deque([(i, j)]);
    #a-색약X b-색약O
    current = colors[i][j];
    compareL = [(1, 0), (-1, 0), (0, 1), (0, -1)];

    while queue:
        x, y = queue.popleft();
        for x1, y1 in compareL:
            mx, my = x1+x, y1+y;
        
            if mx < 0 or mx >= N: continue;
            if my < 0 or my >= N: continue;

            compare = colors[mx][my];
            if visit[mx][my]: continue;

            if current == compare or (kind == 2 and current != "B" and compare != "B"):
                queue.append((mx, my));
                visit[mx][my] = True;
        
N = int(input());

colors = [ list(input()) for _ in range(N)];
visit = [[False]*N for _ in range(N)];
a, b = 0, 0;

for i in range(N):
    for j in range(N):
        if visit[i][j]: continue;
        bfs(i, j);
        a+=1;
        
visit = [[False]*N for _ in range(N)];
for i in range(N):
    for j in range(N):
        if visit[i][j]: continue;
        bfs(i, j, 2);
        b+=1;

print(a, b);