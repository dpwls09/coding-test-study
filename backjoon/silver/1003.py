# 한번에 다 구하고 계산함.. -> 나중에 범위크면 메모리 초과날 수도 있음
# 바로바로 계산하자~

zeroCount = [0]*41;
oneCount = [0]*41;

zeroCount[0] = 1;
oneCount[1] = 1;

for n in range(2, 41):
    zeroCount[n] = zeroCount[n-1] + zeroCount[n-2];
    oneCount[n] = oneCount[n-1] + oneCount[n-2];

T = int(input());

for _ in range(T):
    N = int(input());
    print(zeroCount[N], oneCount[N]);
