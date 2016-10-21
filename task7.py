# Наименьшее число m, такое, что m! делится без остатка на 10 — это m=5 (5! = 120). Аналогично, наименьшее число m, такое, что m! делится без остатка на 25 — это m=10. В общем случае, значение функции s(n) равно наименьшему числу m, такому что m! без остатка делится на n. Определим функцию S(M, N) = ∑s(n) для всех n ∈ [M, N]. К примеру, S(6, 10) = 3 + 7 + 4 + 6 + 5 = 25. Найдите S(610000000, 620000000).
# S(2100000, 2200000).
# ответ: 25350299815


import time
import math
# главная функция
def S(N, M):
    result = 0
    list = generate(int(math.sqrt(M)) + 1000)
    for i in range(N, M + 1):
        result += s(factorization(i, list))
    return result


# функция принимает число n в виде словаря простых чисел и их степеней и выдает минимальное m такое, что m!%n==0
def s(n):
    result = 0
    for (num, exp) in n.items():
        tmp = get_fact(num, exp)
        if tmp > result:
            result = tmp
    return result


# функция принимает число и степень, и возвращает минимальное m такое, что m! %(число**степень) == 0
def get_fact(num, exp):
    a = 1
    res = num
    while (a < exp):
        res += num
        a += get_exp(res, num)
    return res


def get_exp(num, base):
    exp = 1
    while ((num // base) % base == 0):
        num = num // base
        exp += 1
    return exp


# разложить число на простые множители
def factorization(num, primes_list):
    primes_dict = {}
    i = 0
    a = primes_list[i]
    while a * a <= num:
        if num % a == 0:
            if primes_dict.get(a):
                primes_dict[a] += 1
            else:
                primes_dict[a] = 1
            num //= a
        else:
            i += 1
            a = primes_list[i]
    if num != 1:
        if primes_dict.get(num):
            primes_dict[num] += 1
        else:
            primes_dict[num] = 1
    return primes_dict


# создать список простых чисел (решето Эратосфена)
def generate(m):
    a = list(range(m + 1))
    prime_num = []
    i = 2
    while i <= m:
        if a[i] != 0:
            prime_num.append(a[i])
            for j in range(i, m + 1, i):
                a[j] = 0
        i += 1
    return prime_num


print(S(2100000, 2200000))

