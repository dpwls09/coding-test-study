# union-find 알고리즘 사용....
#내가 첫번째로 풀었던 코드에서 
import sys;
input = sys.stdin.readline;
def gate_find(max):
    if gate[max] != max:
        gate[max] = gate_find(gate[max]);

    return gate[max];

def union(a, b):
    b_root = gate_find(b);
    gate[a] = b_root;

G = int(input());
P = int(input());

gate = [i for i in range(G+1)];
maxList = [ int(input().rstrip()) for _ in range(P)]; #인덱스는 0부터 시작하기때무네~
result = 0;

for max in maxList:
    root = gate_find(max);

    if root == 0:
        break;

    union(root, root-1);
    result += 1;

print(result);
        



# #이진탐색쓰면 시간 줄어들까?
# #input() -> sys.stdin.readline 변경
# # from collections import deque;
# import sys;
# input = sys.stdin.readline;

# G = int(input());
# P = int(input());

# #인덱스는 0부터 시작하기때무네 +1해줌
# gate = [i+1 for i in range(G)];
# maxList = [ int(input()) for _ in range(P)];
# result = 0;
# # gate = deque(gate);

# for max in maxList:
#     if gate[0] > max:
#         print(result);
#         exit(0);

#     start = 0;
#     end = len(gate);

#     while start < end:
#         mid = (start + end)//2;

#         if max < gate[mid]:
#             end = mid
#         else:
#             start = mid+1

#     gate.remove(gate[start-1]);
#     result += 1;
    
    


#도킹할 위치를 찾는부분에서 시간초과 된건가?
#가장 긴 수열 알고리즘 써야하나??

# def isDocking(max):
#     while max >= 0:
#         if gate[max] == False:
#             gate[max] = True;
#             return True;
#         max -= 1;
#     return False;

# G = int(input());
# P = int(input());

# gate = [False for _ in range(G)];
# maxList = [ int(input())-1 for _ in range(P)]; #인덱스는 0부터 시작하기때무네~
# docking = [];

# result = 0;

# for max in maxList:
#     if len (docking) == 0:
#             docking.append(max);
#             continue;
#     start = 0;
#     end = len(docking);
#     while start < end:
#         mid = (start + end)//2;

#         if max < docking[mid]:
#             end = mid
#         else:
#             start = mid+1
    
#     docking.insert(start, max);





# 시간초과
def isDocking(max):
    while max >= 0:
        if gate[max] == False:
            gate[max] = True;
            return True;
        max -= 1;
    return False;

G = int(input());
P = int(input());

gate = [False for _ in range(G)];
maxList = [ int(input())-1 for _ in range(P)]; #인덱스는 0부터 시작하기때무네~
result = 0;

for max in maxList:
    if isDocking(max):
        result += 1;
    else:
        print(result)
        exit(0);
    
    



#틀림
# G = int(input());
# P = int(input());

# gate = [False for _ in range(G)];
# maxList = [ int(input())-1 for _ in range(P)]; #인덱스는 0부터 시작하기때무네~
# min = 0;

# for max in maxList:
#     if min <= max:
#         gate[min] = True;
#         min += 1;
#     else:
#         print(min);
#         exit(0);