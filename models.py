import sys

task = sys.stdin.readlines()
out = open("D-small.out", "w")
i = 1
count = 1
while i < len(task):
    line = task[i].split(" ")
    n = int(line[0])
    m = int(line[1])
    adigs = {}
    adi = {}
    ddigs = {}
    ddi = {}
    ri = {}
    ci = {}
    crosses = {}
    pluses = {}
    pts = 0
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if c + r in adigs:
                adigs[c + r].append((r, c))
            else:
                adigs[c + r] = [(r, c)]
            if c - r in ddigs:
                ddigs[c - r].append((r, c))
            else:
                ddigs[c - r] = [(r, c)]
    i += 1
    for j in range(i, i + m):
        line = task[j].split(" ")
        r = int(line[1])
        c = int(line[2])
        if line[0] != '+':
            ri[r] = 1
            ci[c] = 1
            pts += 1
            crosses[(r, c)] = -1
        if line[0] != 'x':
            adi[c + r] = 1
            ddi[c - r] = 1
            pts += 1
            pluses[(r, c)] = -1
    i += m

    for r in range(1, n + 1):
        if r in ri:
            continue
        for c in range(1, n + 1):
            if c in ci:
                continue
            ci[c] = 1
            crosses[(r, c)] = 1
            pts += 1
            break
    for k in ddigs:
        if k in ddi:
            continue
        md = n
        y = -1
        x = -1
        for r, c in ddigs[k]:
            if c + r in adi:
                continue
            ln = len(adigs[c + r])
            if ln <= md:
                md = ln
                y = r
                x = c
        if y > 0:
            adi[x + y] = 1
            pluses[(y, x)] = 1
            pts += 1
    models = 0
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if crosses.get((r, c), 0) > 0 or pluses.get((r, c), 0) > 0:
                models += 1

    print "Case #", count, ": ", pts, " ", models
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if crosses.get((r, c), 0) > 0 or pluses.get((r, c), 0) > 0:
                if (r, c) in crosses:
                    if (r, c) in pluses:
                        print "o", " ", r, " ", c
                    else:
                        print "x", " ", r, " ", c
                else:
                        print "+", " ", r, " ", c
    count += 1
