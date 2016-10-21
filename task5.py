m = 10341  # число, от которого ищем S(m)
# создание списка простых чисел до m (решето Эратосфена)
a = list(range(m + 1))
prime_num = []
i = 2
while i <= m:
    if a[i] != 0:
        prime_num.append(a[i])
        for j in range(i, m + 1, i):
            a[j] = 0
    i += 1

matrix = [[0] * m for i in range(m)]

result = 0
for i in range(m):
    if (i + 1) in prime_num:
        matrix[0][i] = 1
        result += 1

for n in range(m):
    half_n = n // 2
    for k in range(1, half_n + 1):
        for i in range(n - 1):
            if matrix[0][i] and matrix[k - 1][n - i - 1]:
                result += 1
                matrix[k][n] = 1
                break

print(result)
