import sys;
input = sys.stdin.readline;

N, M = map(int, input().strip().split());
numList = list(map(int, input().strip().split()));
sumList = [0];

for i, num in enumerate(numList, 1):
    sumList.append(sumList[i-1]+num);

for _ in range(M):
    i, j = map(int, input().strip().split());
    print(sumList[j]-sumList[i-1]);