from collections import deque;

def bfs (start, finish):
    queue = deque([]);
    visit = {};
    visit[start] = True;
    queue.append(start);

    while queue:
        node = queue.pop();
        
        for n in graph[node]:
            if n == finish:
                return 1;

            if n not in visit:
                queue.append(n);
                visit[n] = True;
    return 0;

N = int(input());
graph = [[] for _ in range(N)];
result = [[0]*N for _ in range(N)];

for i in range(N):
    for j, v in enumerate(list(map(int, input().split()))):
        result[i][j] = v;
        if v == 1:
            graph[i].append(j);

#경로 여부 표시
for i, v1 in enumerate(result):
    for j, v in enumerate(v1):
        
        if v == 1: continue;

        p = bfs(i, j);
        result[i][j] = p;
        if p == 1 and j not in graph[i]:
            graph[i].append(j);

#출력
for row in result:
    print(*row, sep=' ',end='\n');
    

# import sys
# input = sys.stdin.readline

# def findRoad():
#     n = int(input())
#     road = {i:[] for i in range(n)}
#     for i in range(n):
#         road[i] += list(map(int, input().split()))
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if road[i][j] == 0 and road[i][k] == 1 and road[k][j] == 1:
#                     road[i][j] = 1
#     for i in range(n):
#         print(*road[i],sep=" ")
#     return

# if __name__ == "__main__":
#     findRoad()

