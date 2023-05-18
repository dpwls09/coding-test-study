#오름차순 정렬하는것 같음 거기에 dp

def binary(t):
    start = 0
    end = len(sorted_time);

    while start < end:
        mid = (start+end)//2;

        if sorted_time[mid] == t:
            start = mid
            break;

        if sorted_time[mid] < t:
            start = mid+1;
        else:
            end = mid;

    sorted_time.insert(start, t);

N = int(input());
time = list(map(int, input().split()));
sorted_time = [];
dp = [0 for _ in range(N)];
total = 0;

for T in time:
    binary(T);

dp[0] = sorted_time[0];
total = dp[0];

for i in range(1, N):
    dp[i] = dp[i-1]+sorted_time[i];
    total += dp[i];

print(total);