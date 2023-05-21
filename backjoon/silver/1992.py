import sys;

input = sys.stdin.readline;
result = "";
def checkNumber(v):
    length = len(v);
    compare = v[0][0];

    for y in range(length):
        for x in range(length):
            if compare != v[y][x]:
                return False;

    return True;

def division(v):
    w = len(v)//2;

    for i in range(2):
        Y = i*w
        for j in range(2):
            X = j*w;
            quadTree([ sm_v[X:X+w] for sm_v in v[Y:Y+w]]);

def quadTree(v):
    global result;
    if checkNumber(v):
        result += v[0][0];
    else:
        result += "(";
        division(v);
        result += ")"


N = int(input().strip());
video = [input().strip() for _ in range(N)];

quadTree(video);
print(result);