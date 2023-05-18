import sys;

def cutting(paper):
    interval = len(paper[0])//3;

    for j in range(3):
        h = j*interval
        for i in range(3):
            w = i*interval;
            small = [ paper[i][w:w+interval] for i in range(h,h+interval)];
            check(small);

def check(paper):
    compare = paper[0][0];

    for i in paper:
        for p in i:
            if compare != p:
                cutting(paper);
                return;
    
    result[str(compare)] += 1;


input = sys.stdin.readline;
N = int(input().strip());

result = {'-1':0, '0':0, '1':0};

paper = [ list(map(int, input().strip().split())) for _ in range(N)]
check(paper);
print(result['-1']);
print(result['0']);
print(result['1']);

