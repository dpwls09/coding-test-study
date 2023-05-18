#다익스트라 알고리즘은 일단 노드들 간 이동이 가능한 경로 정보를 다 변수에 저장해둠. 그리고
#시작 지점을 기준으로 갈 수 있는 모든 노드들의 최단경로를 탐색다 해둠
# 도착점까지의 거리를 기록할 변수 따로 선언해두기

import heapq;

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start));

    distance[start] = 0;

    while queue:
        dist, node = heapq.heappop(queue);
        
        if distance[node] < dist: continue;

        for f, d in graph[node]:
            cost = distance[node]+d;
            if cost < distance[f]:
                distance[f] = cost;
                heapq.heappush(queue, (cost, f));


N, D = map(int, input().split());

# index: 시작위치, [(value[0]: 도착위치, value[1]: 거리), ...]
graph = [[(i+1, 1)] for i in range(D+1)];
graph[-1]=[];
distance = [10001]*(D+1)

for _ in range(N):
    s, f, d = list(map(int, input().split()));
    if f>D : continue;

    graph[s].append((f, d));

dijkstra(0);
print(distance[D]);