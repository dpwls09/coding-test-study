# 우선순위 큐 -> 힙으로 풀기. 
# 파이썬에서는 최소힙만 있음!
# 이중 우선순위일 경우 2개의 힙 만들어서 두개를 동기화작업하는것이 중요함. 
# input 보다 sys.stdin.readline 쓰자...
# 처음에는 숫자를 넣을때마다 오름차순으로 정렬하면서 넣음 -> 시간 초과된 원인.
# => 문제에서는 최대 최소값만 구하면 됨. 왜 정렬하려고 했니.. 문제 요점파악 잘하자~ 
# 최대 최소 값나오면 최대힙, 최소힙 떠올리기!!!

import sys
import heapq;

T = int(sys.stdin.readline());

for _ in range(T):
    minq = [];
    maxq = [];
    k = int(sys.stdin.readline());
    deleteList = [False]*k;

    for i in range(k):
        o, v = sys.stdin.readline().split();
        v = int(v);

        if o == "I":
            heapq.heappush(minq, (v,i));
            heapq.heappush(maxq, (-v,i));
        else:
            if v == 1:
                while maxq:
                    value, id =  heapq.heappop(maxq);
                    if not deleteList[id]:
                        deleteList[id]=True;
                        break;
            else:
                while minq:
                    value, id =  heapq.heappop(minq);
                    if not deleteList[id]:
                        deleteList[id]=True;
                        break;

    while maxq and deleteList[maxq[0][1]]:
        heapq.heappop(maxq);
    while minq and deleteList[minq[0][1]]:
        heapq.heappop(minq);

    if maxq and minq:
        print(-maxq[0][0], minq[0][0]);
    else: print('EMPTY');


# T = int(input());
# queue = [];

# def enqueue(v):

#     L = len(queue);
#     start = 0;
#     end = L-1;
#     index = -1;
# 2진탐색
#     while start <= end:
#         mid = (start + end)//2;

#         if v < queue[mid]: #중간값보다 작을 경우
#             end = mid-1;
#         elif v == queue[mid]:
#             index = mid;
#             break;
#         else:
#             start = mid+1;

#     if index != -1: queue.insert(index, v); #같은 값이 존재할 경우
#     elif end == -1: queue.insert(0, v); #v가 최솟값일 경우
#     elif start == len(queue): queue.append(v); #v가 최대값일 경우
#     else: queue.insert(start, v);


# for _ in range(T):
#     k = int(input());
#     queue.clear();

#     for _ in range(k):
#         o, v = input().split();
#         v = int(v);
#         if o == 'I':
#             enqueue(v);
#         elif o == "D":
#             if len(queue) == 0: continue;

#             if v == 1:
#                 queue.pop(len(queue)-1);
#             else:
#                 queue.pop(0);

#     if (len(queue)==0): print('EMPTY');
#     else: print(queue[len(queue)-1],queue[0]);