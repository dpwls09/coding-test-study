# # 조규현 x1,y1,r1  백승환 x2,y2,r2 류재명 좌표 x3,y3
# # 원 방정식 (x3-x1)^ +  (y3-y1)^ = r^

# import sys,math;
# input = sys.stdin.readline;

# case = int(input());

# while case > 0:
#     x1,y1,r1,x2,y2,r2 = map(int, input().split());

#     # 두 점 사이의 거리
#     d = math.sqrt((x1-x2)**2 + (y1-y2)**2);

#     #중심이 같을 경우
#     if d==0:
#         if r1==r2:
#             print(-1);
#         else:
#             print(0)
#     #중심이 다를 경우
#     else:
#         # 한 점에서 만날 경우
#         if r1+r2==d or abs(r2-r1)==d:
#             print(1);
#         # 두 점에서 만날 경우
#         elif abs(r1-r2) < d and d < r1+r2:
#             print(2);
#         # 만나지 않을 경우
#         else:
#             print(0);

#     case = case-1;

#     # 조규현 x1,y1,r1  백승환 x2,y2,r2 류재명 좌표 x3,y3
# # 원 방정식 (x3-x1)^ +  (y3-y1)^ = r^

import math;

case = int(input());

while case > 0 :
    x1,y1,r1,x2,y2,r2 = map(int, input().split(' '));

    # 두 점 사이의 거리
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2);

    #한 점에서 만날 경우
    if r1+r2 == d or abs(r1-r2)==d:
        print(1);
    #두 점에서 만날 경우
    elif abs(r1-r2) < d < r1+r2:
        print(2);
    #만나지 않는 경우
    elif r1+r2 < d or abs(r1-r2) > d or (d==0 and r1!=r2):
        print(0);
    #같은 원일 경우
    elif r1==r2 & d==0:
        print(-1)
    else:
        print(-1)

    case = case-1;
