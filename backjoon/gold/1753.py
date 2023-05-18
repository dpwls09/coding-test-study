import heapq;
import sys;

input = sys.stdin.readline;

def dijkstra(start):
    queue = [];
    heapq.heappush(queue, [0, start]);
    now = start;
    distance[start]=0;

    while queue:
        w, v = heapq.heappop(queue);
        
        if w > distance[v]: continue;

        for next_v, next_w in graph[v]:
            cost = distance[v] + next_w;
            if cost < distance[next_v]:
                distance[next_v] = cost;
                heapq.heappush(queue, [cost, next_v]);


V, E = map(int, input().strip().split());
start = int(input().strip());
graph = [[] for _ in range(V+1)];
distance = [10**7]*(V+1);

for _ in range(E):
    u, v, w = map(int, input().strip().split());
    graph[u].append([v, w]);

dijkstra(start);

for i in range(V):
    dist = distance[i+1];
    if dist == 10**7:
        print('INF');
    else:
        print(dist);