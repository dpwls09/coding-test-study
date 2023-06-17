N = int(input());

num = [0]*(N+2);
num[1], num[2] = 1, 3;

for n in range(3, N+1):
    num[n] = num[n-1] + num[n-2]*2;

print(num[N]%10007);