import collections
import sys

task = sys.stdin.readlines()
c = 1
for line in task[1:]:
    line = line.split(" ")
    n = int(line[0])
    k = int(line[1])
    stalls = collections.OrderedDict()
    stalls[n] = 1
    ls = -1
    rs = -1
    while k > 0:
        size, num = stalls.popitem(last=False)
        ls = (size - 1) / 2
        rs = size / 2
        if rs in stalls:
            stalls[rs] += num
        else:
            stalls[rs] = num
        if ls in stalls:
            stalls[ls] += num
        else:
            stalls[ls] = num
        k -= num
    print "Case #", c, ": ", max(ls, rs), " ", min(ls, rs)
    c += 1
