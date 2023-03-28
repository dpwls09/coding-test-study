# 이 문제를 풀면서 느낀점
# 반복적인? 누적되는 계산이 많다면 차라리 계산값을 저장해두자.
# 그럼 저장된 계산결과를 계속 꺼내 쓰면 중복적으로 계산하는걸 막을수 있음
# => 시간 줄일 수 있음 !


#소수인지 판별하는 함수
def BB(num):
    if num == 1:
        return False;

    n = 2;
    while (n <= num):
        if num % n == 0 :
            if num != n : 
                return False;
            else :
                return True;
        else:
            n += 1;

    return False;

#소인수분해 함수
def AA(num): #소인수분해
    n = 2;
    count=0;

    while (True):
        if num >= n:
            if num % n == 0:
                count += 1;
                num = num//n;
            else :
                n += 1;
        else :
            break;
    
    return count;

#소수인지 판별하는 함수 + 1부터 루트num까지만 확인함
def CC(num):
    if num == 1: return False;

    n=2;
    while n*n <= num:
        if num % n == 0 :
            return False;
        n += 1;

    return True;

A,B = map(int, input().split());

#미리 소수인 수들을 다 구하고 
# 소수인지 아닌지 True False 로 구분.
# d -> index: 숫자, value: 숫자가 소수인지 판별하는 값. boolean
d = [False for _ in range(100001)];

for i in range(1, 100001):
    if CC(i) : d[i]=True;

# 소인수분해 개수의 최소값은 1임
# dd -> index: 숫자, value: 숫자의 소인수분해의 개수
dd=[];
for i in range(B+1):
    if d[i]: dd.append(1); #i가 소수일 경우 dd[i]에 1 넣음. 
    else: dd.append(0);

for i in range(2, B+1):
    for j in range(2, B+1):
        if i*j > B: break;
        if d[j]:
            dd[i*j] = dd[i] + 1;

count = 0;
for i in range(A,B+1):
    if d[dd[i]]:
        count += 1;

print(count);
