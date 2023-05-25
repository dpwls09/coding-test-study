T = int(input());

def calc (M, N, x, y):
    while x <= M*N :
        if x%N == y%N:
            return x;

        x += M;
    return -1;

for _ in range(T):
    M, N, x, y = map(int, input().split());

    print(calc(M, N, x, y));



# from collections import deque;

# T = int(input());
# resultList = []

# for _ in range(T):
#     M, N, x, y = map(int, input().split());
    
#     M_queue = deque([i for i in range(1, M+1)]);
#     N_queue = deque([i for i in range(1, N+1)]);
    
#     result = 0;
#     x1, y1 = 0, 0;
    
#     while True:
#         if x1 == x and y1 == y: break;

#         if x1 == M and y1 == N:
#             result = -1;
#             break;

#         x1 = M_queue.popleft();
#         y1 = N_queue.popleft();

#         M_queue.append(x1);
#         N_queue.append(y1);

#         result += 1;
    
#     resultList.append(result);

# for result in resultList:
#     print(result);