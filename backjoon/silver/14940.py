from collections import deque;
def bfs(i, j, depth):
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)];
    next = []

    for y, x in move:
        my, mx = y+i, x+j;

        if my < 0 or mx < 0 or my >= N or mx >= M: continue;
        if graph[my][mx] == 0 or graph[my][mx] == 2: continue;
        if result[my][mx] != -1: continue;

        result[my][mx] = depth;
        next.append((my, mx));

    return next;


N, M = map(int, input().split());

graph = [];
result = [[-1]*M for _ in range(N)];
target = [-1, -1];

for i in range(N):
    numList = list(map(int, input().split()));
    graph.append(numList);

    for j in range(M):
        if numList[j] == 2: target = [i, j];
        elif numList[j] == 0: result[i][j] = 0;


result[target[0]][target[1]] = 0;
queue = deque([]);
group = [(target[0], target[1])];
depth = 1;

while group:
    queue.extend(group);
    group = [];
    while queue:
        i, j = queue.pop();
        group.extend(bfs(i, j, depth));
    depth += 1;
    
for n in result:
    print(" ".join(map(str, n)));