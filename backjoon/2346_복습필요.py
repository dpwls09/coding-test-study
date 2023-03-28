N = int(input());
L = list(map(int, input().split()));

resultList = '1';
move = L[0];
i = 0;
L[0] = False;
FalseNum = 1;

while True:
    count = 0;
    if FalseNum == N:
        break;

    while True:

        if count == abs(move): break;

        if move < 0:
            i = i-1;
        else:
            i = i+1;
            
        if i < 0:
            i = N-(abs(i)%N);
        else:
            i = i%N;
        
        if L[i] != False:
            count+=1
    
    move = L[i];
    resultList += " "+str(i+1);
    L[i] = False;
    FalseNum += 1;


print(resultList);
