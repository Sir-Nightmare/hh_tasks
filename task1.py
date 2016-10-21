i = 0
for s in range(1, 10):
    for y in range(0, 10):
        for r in range(0, 10):
            for x in range(0, 10):
                for v in range(1, 10):
                    if 200 * s + 9 * y + 11 * x + r == 110 * v:
                        checkSet = {s, y, r, x, v}
                        if len(checkSet) == 5:
                            print(str(s) + str(y) + str(x) + '+' + str(s) + str(x) + str(r) + '=' +
                                  str(v) + str(v) + str(y))
                            i += 1
print(i)
