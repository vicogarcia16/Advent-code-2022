from itertools import islice

with open("data/3.in") as f:
    ls = [x.strip() for x in f.readlines()]


def score(o):
    return ord(o) - ord("a") + 1 if o.islower() else ord(o) - ord("A") + 27


#* Part 1
s = 0
for l in ls:
    mid = len(l) // 2
    p1, p2 = l[:mid], l[mid:]
    (o,) = set(p1) & set(p2)
    s += score(o)
print(s)

#* Part 2
sets = map(set, ls)
s = 0
for _ in range(len(ls) // 3):
    g1, g2, g3 = islice(sets, 3)
    (o,) = g1 & g2 & g3
    s += score(o)
print(s)