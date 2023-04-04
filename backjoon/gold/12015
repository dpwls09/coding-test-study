import sys
input = sys.stdin.readline;

N = int(input());
A = list(map(int, input().split()));

# dp = [0 for _ in range(1000001)];
# dp[A[0]] = 1;

# for i in A:
#     dp[i] = max(dp[:i])+1;

# print(max(dp));

# 오히려 이렇게 하는게 더 빠를려나?!
# dp = [0 for _ in range(N)];
# dp[0] = 1;
# for i in range(1, N):
#     for j in range(i):
#         if A[i] > A[j]:
#             dp[i] = max(dp[j]+1, dp[i]);
# print(max(dp));

#max(dp[:i])부분을 변경해야할듯.
#if 로 조건을 주면 어떨까?! -> 1% 오르고 시간초과..
# dp = [0 for _ in range(1000001)];
# visit = [False for _ in range(1000001)];

# dp[A[0]] = 1;

# for i in A:
#     dp[i] = max(dp[:i])+1
#     if 1000000-i < dp[i]: break;

# print(max(dp));

#저렇게 브레이크 포인트 주는거 괜찮은것 같은디..ㄴㄴ
# dp = [0 for _ in range(1000001)];
#이거는 걍 틀렸음
# dp = [[A[0], 1]]; #(수열의 마지막 값, 수열의 길이)

# for i in range(1, N):
#     flag = False;
#     for j in range(len(dp)):
#         last, length = dp[j];

#         if A[i] > last:
#             dp[j][0] = A[i];
#             dp[j][1] = length+1;
#             flag = True;

#     if flag==False:
#         dp.append([A[i], 1]);


# V, L = zip(*dp);
# print(max(L));

dp = [0];

for i in A:
    if dp[-1] < i:
        dp.append(i);
        continue;

    left = 0;
    right = len(dp);

    while right > left:
        mid = (right+left)//2;
        if dp[mid] < i:
            left = mid+1;
        else:
            right = mid;

    dp[right] = i;

print(len(dp)-1);


