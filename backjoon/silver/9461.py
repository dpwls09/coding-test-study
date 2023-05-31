import sys;

input = sys.stdin.readline;
P = [0 for _ in range(100)];
init = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9];

def make_p ():
    for i in range(10):
        P[i] = init[i];

    for i in range(10, 100):
        P[i] = P[i-1] + P[i-5];

make_p();

T = int(input().strip());

for _ in range(T):
    N = int(input().strip());
    print(P[N-1]);