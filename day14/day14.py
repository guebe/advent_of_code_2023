import numpy as np

def weight(a):
    res = 0
    for x in a:
        res += sum(len(x)-i if s=='O' else 0 for i,s in enumerate(x))
    return res

def slide(a):
    for x in a:
        do_work = True
        while (do_work):
            do_work = False
            for i in range(1,len(x)):
                if (x[i-1] == "." and x[i] == "O"):
                    x[i-1], x[i] = x[i], x[i-1]
                    do_work = True

a = np.array([list(line.strip()) for line in open("input").readlines()])
a = np.transpose(a)
slide(a)
print(weight(a))
