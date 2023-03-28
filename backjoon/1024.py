# N,L = map(int, input().split());
# resultList = [];
# while L<=100:

#     a,b=divmod(N,L) #a=몫  b=나머지

#     #L이 홀수일때
#     if L%2 == 1: 
#         if b != 0:
#             L=L+1;
#             continue;
#         else:
#             c = int(((L-1)/2)*(-1)); #빼는 값

#             if a+c < 0 :
#                 L=L+1;
#                 continue;

#             for _ in range(L):
#                 resultList.append(str(a+c));
#                 c=c+1;
#             print(" ".join(resultList));
#             break;
#     #L짝수일때
#     else:
#         if b == 0 or L/2!=b:
#             L=L+1;
#             continue;

#         c = -b+1

#         if a+c == 0 :
#             L=L+1;
#             continue;

#         for _ in range(L):
#             resultList.append(str(a+c));
#             c = c+1;
#             if c == b-1: 
#                 c=b
#         print(" ".join(resultList));
#         break;

# if L > 100:
#     print(-1);


#등차수열의 합 S = n{2a+(n-1)d}/2
# a = {2S-n(n+1)}/2n

N,L = map(int, input().split());

returnData = ""

while(L<=100):
    a = (2*N-L*(L-1))/(2*L);
    b=int(a);
    c= a-b;

    if a < 0 or c!=0: 
        L+=1
    else :
        for i in range(L):
            returnData += str(int(b))
            a+=1
            b=a
            if i == L-1: break;

            returnData += " "

        print(returnData);
        break;

if L>100:
    print(-1);



