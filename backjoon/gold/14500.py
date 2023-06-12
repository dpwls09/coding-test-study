# def rotation(shape, kind):
#     result = [];

#     for i in range(kind):
#         result.append([direction[(s+i)%4] for s in shape]);
    
#     return result;

# def symmetrical(shape, check):

#     if check == False: return [shape];

#     result = [shape, []];

#     for s in shape:
#         if s==1: s=3;
#         elif s==3: s=1;

#         result[1].append(s);
    
#     return result;

# def makeAllShape():

#     result = []

#     for num in range(5):
#         shape = tet[num]
#         for rot_shape in rotation(shape, rotate[num]):
#             for sym_shape in symmetrical(rot_shape, symmetry[num]):
#                 result.append(sym_shape);

#     return result;

# def calc(shape, i, j):
#     max_sum = paper[i][j];

#     for n in shape:
#         if direction


# N, M = map(int, input().split());
# paper = [[map(int, input().split())] for _ in range(N)];
# direction = [(1, 0), (0, 1), (-1, 0), (0, -1)];
# #       ㅡ         ㅁ           ㄴ         ㄹ          ㅜ
# tet = [[1, 1, 1], [1, 2, 3], [2, 2, 1], [2, 1, 2], [1, 2, [1, 0]]];
# rotate = [2, 1, 4, 2, 4];
# symmetry = [False, False, True, True, False];

# for i in range(N):
#     for j in range(M):

max_sum = 0;
N, M = map(int, input().split());
paper = [list(map(int, input().split())) for _ in range(N)];
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)];
visit = [[False]*M for _ in range(N)];

def dfs (y, x, sum, depth):

    global max_sum;

    if depth == 3:
        max_sum = max(max_sum, sum);
        return;
    
    for dy, dx in direction:
        y1, x1 = y+dy, x+dx;
        
        if y1 < 0 or y1 >= N or x1 < 0 or x1 >= M or visit[y1][x1]:
            continue;
        
        visit[y1][x1] = True;

        #ㅗ 예외처리
        if depth == 1:
            dfs(y, x, sum + paper[y1][x1], depth+1);
            visit[y1][x1] = False;

        dfs(y1, x1, sum + paper[y1][x1], depth+1);
        visit[y1][x1] = False;

for i in range(N):
    for j in range(M):
        visit[i][j] = True;
        dfs(i, j, paper[i][j], 0);
        visit[i][j] = False;
        # visit = [[False]*M for _ in range(N)];

print(max_sum);




