import sys

task = sys.stdin.readlines()
c = 1
f = 0
for line in task[1:]:
    pk = line.split(" ")
    oz = []
    for p in pk[0]:
        if p == "-":
            oz.append(0^0)
        else:
            oz.append(1^0)
    k = int(pk[1])
    n = 0
    for i in range(len(oz)):
        if oz[i] == 0:
            if i + (k - 1) >= len(oz):
                out.write("Case #" + str(c) + ": IMPOSSIBLE\n")
                f = 1
                break
            for j in range(i, i+k):
                oz[j] = oz[j]^1
            n += 1
    if f == 0:
        print "Case #", c, ": ", n
    f = 0
    c += 1
