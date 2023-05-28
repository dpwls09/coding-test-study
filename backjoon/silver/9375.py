import sys;

input = sys.stdin.readline;

T = int(input().strip());

for _ in range(T):
    n = int(input().strip());
    closet = {};
    result = 1;

    #옷 종류만큼 추가
    for _ in range(n):
        name, clothing = input().strip().split();

        if clothing not in closet:
            closet[clothing] = 2;
        else:
            closet[clothing] += 1;
        
    for value in closet.values():
          result *= value;
    
    print(result-1);