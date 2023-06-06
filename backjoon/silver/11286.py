import sys;
import heapq;

input = sys.stdin.readline;

N = int(input().strip());
arr = [];

for _ in range(N):
    x = int(input().strip());

    if x == 0:
        if not arr:
            print(0);
        else:
            print(heapq.heappop(arr)[1]);
    else:
        if x < 0:
            y = x+0.5;
            heapq.heappush(arr, (-y, x));
        else: 
            heapq.heappush(arr, (x, x));