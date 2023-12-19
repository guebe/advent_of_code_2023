# This solution uses eval to parse dictionary and to evaluate the conditions.
# The final condition in each line is encoded as always True to avoid spectial
# handling.
import re

def parse_file():
    sect1, sect2 = open("input").read().split("\n\n")

    workflows = {}
    for line in sect1.split():
        key, blocks = line.replace("}","").split("{")
        workflows[key] = [b.split(":") if ":" in b else ("True", b) for b in blocks.split(",")]

    part_ratings = [eval(re.sub('([a-z])=', "'\\1':", line)) for line in sect2.split()]

    return workflows, part_ratings

def recurse(part, startkey):
    for cond, key in workflows[startkey]:
        x,m,a,s = part['x'], part['m'], part['a'], part['s']
        if (eval(cond)):
            if key == 'A':
                return 1
            elif key == 'R':
                return 0
            else:
                return recurse(part, key)
        else:
            pass
    assert False

res = 0
workflows, part_ratings = parse_file()
for part in part_ratings:
    if recurse(part, 'in'):
        res += part['x'] + part['m'] + part['a'] + part['s']
print(res)
