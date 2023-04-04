# 더 빠른 예시
import sys
read = sys.stdin.readline

n = int(read())
dp = [0] * 1001
num_list = list(map(int, read().split()))

for num in num_list:
    dp[num] = max(dp[:num]) + 1
print(max(dp));

# import sys
# read = sys.stdin.readline;

# N = int(read());
# A = list(map(int, read().split()));
# check = [ 1 for _ in range(N)];
# smallNum = 1001;
# maxCount = 1;

# for i in range(1, N):
#     end = A[i]
#     for j in range(i):
#         preEnd = A[j];

#         if end <= preEnd: continue;

#         check[i] = max(check[i], check[j]+1);

# print(max(check));