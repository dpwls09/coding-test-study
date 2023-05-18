#그리디문젠강?
import heapq;
import sys;

input = sys.stdin.readline;

N = int(input());
time = [];
room = [];

for _ in range(N):
    heapq.heappush(time, list(map(int, input().strip().split())));

while time:
    start, finish = heapq.heappop(time);
    
    if len(room) == 0: 
        heapq.heappush(room, finish);
        continue;
    
    if start < room[0]:
        heapq.heappush(room, finish);
    else:
        heapq.heappop(room);
        heapq.heappush(room, finish);

print(len(room));