# #dp문제인듯??


dp = [0 for _ in range(1001)];
dp[0] = 0;
dp[1] = 1;
dp[2] = 2;

for i in range(3, 1001):
    dp[i] = dp[i-2] + dp[i-1];

N = int(input());
print(dp[N]%10007);