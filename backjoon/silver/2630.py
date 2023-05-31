import sys;

input = sys.stdin.readline;

def cutting(paper):
    width = len(paper[0]);

    sm_paper_list = [];

    for w in range(0,width,width//2):
        for h in range(0,width,width//2):
            sm_paper_list.append([ p[h:h+width//2] for p in paper[w:w+width//2]]);

    return sm_paper_list;


def checkColor(paper):
    width = len(paper[0]);
    sum1 = sum(sum(paper, []));

    if sum1 == 0: return 'white';
    if sum1 == width**2: return 'blue';

    return False;

def classification(paper):

    color = checkColor(paper);

    if color == 'white':
        result[0] += 1;
    elif color == 'blue':
        result[1] += 1;
    else:
        for sm_paper in cutting(paper):
            classification(sm_paper);


N = int(input());
paper = [list(map(int, input().strip().split())) for _ in range(N)];
result = [0, 0];

classification(paper);

print(result[0]);
print(result[1]);