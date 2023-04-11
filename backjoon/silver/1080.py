import sys
input = sys.stdin.readline;

# 아 그냥 비교연산자 써도 되는구나....
# def compare():
#     for i in range(N):
#         for j in range(M):
#             if A[i][j] != B[i][j]:
#                 return False;
    
#     return True;

def conversion(n, m):
    for x in range(n, n+3):
        for y in range(m, m+3):
            if A[x][y] == 0 : A[x][y] = 1;
            else: A[x][y] = 0;

N, M = list(map(int, input().split()));

A = [ list(map(int, input().strip())) for _ in range(N)];
B = [ list(map(int, input().strip())) for _ in range(N)];

if N < 3 or M < 3:
    if A==B: print(0);
    else: print(-1);

    exit(0);

# 최상단 왼쪽에서부터 행렬을 변환할거임.
# 이 풀이가 왜 그리디 알고리즘이냐? 왼쪽상단을 변경하는것은 나머지 행렬들에 영향을 안줌. 
# 그리디하게 푸려면 이런식으로 한쪽 방향을 정해서 맞춰나가야함.
# 근데 그럼 시작점과 반대인 쪽은 마음대로 바꿀 수 없음! 

# 3*3 행렬이 움직일 수 있는 범위 (0,0)부터 시작한다고 했을 경우
# 0 ~ N-2, 0 ~ M-2
count = 0;
for n in range(N-2):
    for m in range(M-2):
        if A[n][m] != B[n][m]: 
            conversion(n, m);
            count += 1;

        if A==B:
            print(count);
            exit(0);
print(-1);