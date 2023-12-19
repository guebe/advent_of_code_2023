import re

def parse_file():
    directions, inputs = open("input").read().split("\n\n")
    ins = []
    for line in inputs.split():
        dict_ = re.sub('([a-z])=', "'\\1':", line)
        dict_ = eval(dict_)
        ins.append(dict_)

    dirs = {}
    for line in directions.split():
        key, values = line.split("{")
        values = values.replace("}","").split(",")
        assert len(values) >= 2
        xxx = []
        for val in values:
            if ":" in val:
                cond, kex = val.split(":")
            else:
                cond, kex = None, val
            xxx.append((cond, kex))
        dirs[key]=xxx
    return ins, dirs

def recurse(i, k):
    start = dirs[k]
    x, m, a, s = i['x'], i['m'], i['a'], i['s']

    for cond, kex in start:
        if not cond:
            if kex == 'A':
                return 1
            elif kex == 'R':
                return 0
            else:
                return recurse(i, kex)
        else:
            if (eval(cond)):
                if kex == 'A':
                    return 1
                elif kex == 'R':
                    return 0
                else:
                    return recurse(i, kex)
            else:
                pass

ins, dirs = parse_file()

sss = 0
for i in ins:
    y = recurse(i, 'in')
    if y:
        sss += i['x'] + i['m'] + i['a'] + i['s']
print(sss)


