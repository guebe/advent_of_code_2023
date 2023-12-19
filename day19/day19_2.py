import re
from copy import deepcopy

def parse_file():
    sect1, sect2 = open("input").read().split("\n\n")

    workflows = {}
    for line in sect1.split():
        key, blocks = line.replace("}","").split("{")
        instr = []
        for b in blocks.split(","):
            if not ":" in b:
                instr.append((None, None, None, b))
            else:
                part1, part2 = b.split(":")
                if ">" in part1:
                    (symbol, value), cond = part1.split(">"), ">"
                elif "<" in part1:
                    (symbol, value), cond = part1.split("<"), "<"
                else:
                    assert False
                instr.append((symbol, cond, int(value), part2))
        workflows[key] = instr 

    return workflows

# accepted input values - multiply the range for each x,m,a,s
# if all parts are accepted the answer is 4000*4000*4000*4000
def accepted(part):
    res = 1
    for range_ in part.values():
        MIN, MAX = range_
        res *= (MAX+1) - MIN
    return res

def recurse(part, startkey):
    res = 0
    for symbol, cond, value, key in workflows[startkey]:
        if not cond: # the last instruction has no condition / is always True
            if key == 'A':
                res += accepted(part)
            elif key == 'R':
                pass
            else:
                res += recurse(part, key)
        else:
            MIN, MAX = part[symbol]
            part_new = deepcopy(part)
            if (cond == ">"):
                if MAX > value:
                    #                 Three possibilities
                    # 1.                      |         MIN......MAX
                    # 2.                MIN...|...MAX
                    # 3. MIN.....MAX          |
                    #                       value
                    # For 2. we have to modify the ranges

                    # we _have_ to split the range in one new part which fits the condition and descends down
                    # and one old range - which we modify to be tried for the next rule
                    # please note that the old range may be empty (if (MIN > value) and (MAX > value))
                    part_new[symbol][0] = max(MIN, value+1) # this part descends down - we have to adopt the MIN value
                    part[symbol][1] = max(MIN, value) # this part does not descend down - we have to adopt the MAX value
                    if key == 'A':
                        res += accepted(part_new)
                    elif key == 'R':
                        pass
                    else:
                        res += recurse(part_new, key)
            elif (cond == "<"):
                if MIN < value:
                    part_new[symbol][1] = min(MAX, value-1)
                    part[symbol][0] = min(MAX, value)
                    if key == 'A':
                        res += accepted(part_new)
                    elif key == 'R':
                        pass
                    else:
                        res += recurse(part_new, key)
            else:
                assert False
    return res

workflows = parse_file()
print(recurse({'x': [1,4000], 'm': [1,4000], 'a': [1,4000], 's': [1,4000]}, 'in'))
