def num_check(n):
    n = [int(a) for a in str(n)]
    i = 0
    temp = 0
    while i < len(n) and temp < len(n):
        k = i
        s = 0
        while k < len(n):
            s += n[k]
            if s == 10:
                temp = k + 1
                break
            if s > 10:
                break
            k += 1
        i += 1
        if i > temp:
            return False
    if s != 10:
        return False
    return True


num = 0
for i in range(1, 5400001):
    if num_check(i):
        num += 1
print(num)
