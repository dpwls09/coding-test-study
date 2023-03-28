#index: number, value: number의 연산 사용 횟수 최솟값.
#기본 셋팅으로는 최소 연산 횟수인 1을 넣어둠.
minOperationList = [0]*(10**6+1);
minOperationList[2], minOperationList[3] = 1, 1;

def makeMinOperationList():

    for i in range(4, 10**6+1):
        subOne = minOperationList[i-1];
        divThree = minOperationList[i//3];
        divTwo = minOperationList[i//2];

        if i%6 == 0:
            if subOne <= divThree:
                if subOne <= divTwo:
                    minOperationList[i] = subOne+1;
                else:
                    minOperationList[i] = divTwo+1;

            elif divThree <= divTwo:
                minOperationList[i] = divThree+1;
            
            else:
                minOperationList[i] = divTwo+1;

        elif i%3 == 0:
            if subOne <= divThree:
                minOperationList[i] = subOne+1;
            else:
                minOperationList[i] = divThree+1;
                
        elif i%2 == 0:
            if subOne <= divTwo:
                minOperationList[i] = subOne+1;
            else:
                minOperationList[i] = divTwo+1;
        else:
            minOperationList[i] = subOne+1;

makeMinOperationList();
num = int(input());
print(minOperationList[num])


# a = int(input())
# d = [0 for _ in range(a+1)]

# for x in range(2, a+1):
#     d[x] = d[x-1] + 1

#     if x % 3 == 0:
#         d[x] = min(d[x], d[x//3] + 1)
#     if x % 2 == 0:
#         d[x] = min(d[x], d[x//2] + 1)

# print(d[a])