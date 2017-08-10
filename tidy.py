import sys

task = sys.stdin.readlines()
c = 1
for line in task[1:]:
    nines = 0
    tidy = list(line)
    tidy = tidy[:len(tidy)-1]
    eq_ind = -1
    i = 0
    cutoff = 0
    while (i < len(tidy)):
        if nines == 1:
            tidy[i] = '9'
        elif i < len(tidy) - 1 and len(tidy) > 1:
            prev = int(tidy[i])
            nxt = int(tidy[i+1])
            if prev > nxt:
                nines = 1
                if eq_ind >= 0:
                    i = eq_ind
                if prev - 1 > 0:
                    tidy[i] = str(prev-1)
                else:
                    cutoff = i + 1
                if prev == nxt and eq_ind == -1:
                    eq_ind = i
                elif prev < nxt and eq_ind >= 0:
                    eq_ind = -1
        i = i + 1

    print "Case #", c, ": ", ''.join(tidy[cutoff:])
    c += 1
