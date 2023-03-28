import sys
import heapq;

N = int(sys.stdin.readline());
hqueue = [];
for _ in range(N):
    X = int(sys.stdin.readline())
    if X > 0:
        heapq.heappush(hqueue, -X);
    else:
        if hqueue:
            print(-heapq.heappop(hqueue));
        else:
            print(0);
        
