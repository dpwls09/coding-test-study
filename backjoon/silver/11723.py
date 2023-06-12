import sys;

input = sys.stdin.readline;

S = set();

def add(x):
    S.add(x);

def remove(x):
    S.discard(x);

def check(x):
    if x in S: print(1);
    else: print(0);

def toggle(x):
    if x in S: S.discard(x);
    else: S.add(x);

def all():
    S = set([i for i in range(1, 21)]);

def empty(x):
    S = set();

M = int(input().strip());

for _ in range(M):
    command = input().strip().split();
    func, x = '', 0;

    if len(command)==1: func = command[0];
    else: func, x = command;

    if func == 'add': S.add(int(x));
    elif func == 'remove': S.discard(int(x));
    elif func == 'check': check(int(x));
    elif func == 'toggle': toggle(int(x));
    elif func == 'all': S = set([i for i in range(1, 21)]);
    elif func == 'empty': S = set();