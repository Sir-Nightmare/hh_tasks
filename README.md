# Задачи первого этапа отбора в школу программирования hh.ru

[**Задача 1**](https://github.com/Sir-Nightmare/hh_tasks/blob/master/task1.py)

Дано равенство, в котором цифры заменены на буквы:  
syx + uus = xsz  
Найдите сколько у него решений, если различным буквам соответствуют различные цифры (ведущих нулей в числе не бывает).

[**Задача 2**](https://github.com/Sir-Nightmare/hh_tasks/blob/master/task2.py)

Число 125874 и результат умножения его на 2 — 251748
можно получить друг из друга перестановкой цифр.

Найдите наименьшее положительное натуральное x такое, что
числа 2*x, 3*x можно получить друг из друга перестановкой цифр.

[**Задача 3**](https://github.com/Sir-Nightmare/hh_tasks/blob/master/task3.py)

Если мы возьмем 47, перевернем его и сложим, получится 47 + 74 = 121 — число-палиндром.  
Если взять 349 и проделать над ним эту операцию три раза, то тоже получится палиндром:  
349 + 943 = 1292  
1292 + 2921 = 4213  
4213 + 3124 = 7337  
Найдите количество положительных натуральных чисел меньших 13073
таких, что из них нельзя получить палиндром за 50 или менее применений
описанной операции (операция должна быть применена хотя бы один раз)

[**Задача 4**](https://github.com/Sir-Nightmare/hh_tasks/blob/master/task4.py)

В некоторых числах можно найти последовательности цифр, которые в сумме дают 10.
К примеру, в числе 3523014 целых четыре таких последовательности:  
3523014  
3523014  
3523014  
3523014  
Можно найти и такие замечательные числа, каждая цифра которых
входит в по крайней мере одну такую последовательность.  
Например, 3523014 является замечательным числом, а 28546 — нет
(в нём нет последовательности цифр, дающей в сумме 10 и при этом включающей 5).

Найдите количество этих замечательных чисел в интервале \[1, 5400000\] (обе границы — включительно).

[**Задача 5**](https://github.com/Sir-Nightmare/hh_tasks/blob/master/task5.py)

Определим функцию P(n,k) следующим образом: P(n,k) = 1, если n может быть представлено в виде
суммы k простых чисел (простые числа в записи могут повторяться, 1 не является простым числом)
и P(n,k) = 0 в обратном случае.  
К примеру, P(10,2) = 1, т.к. 10 может быть представлено в виде суммы 3 + 7 или 5 + 5, а P(11,2) = 0,
так как никакие два простых числа не могут дать в сумме 11.  
Определим функцию S(n) как сумму значений функции P(i,k) для всех i и k, таких что 1≤i≤n, 1≤k≤n.
Таким образом, S(2) = P(1,1) + P(2,1) + P(1,2) + P(2,2) = 1, S(10) = 20, S(1000) = 248838.

Найдите S(13875).

[**Задача 6**](https://github.com/Sir-Nightmare/hh_tasks/blob/master/task6.py)

Рассмотрим все возможные числа ab для 1<a<6 и 1<b<6:  
22=4, 23=8, 24=16, 25=32 32=9, 33=27, 34=81, 35=243 42=16, 43=64, 44=256, 45=1024, 52=25, 53=125, 54=625, 55=3125  
Если убрать повторения, то получим 15 различных чисел.

Сколько различных чисел ab для 2<a<128 и 2<b<116?

[**Задача 7**](https://github.com/Sir-Nightmare/hh_tasks/blob/master/task7.py)

Наименьшее число m, такое, что m! делится без остатка на 10 — это m=5 (5! = 120). 
Аналогично, наименьшее число m, такое, что m! делится без остатка на 25 — это m=10.   
В общем случае, значение функции s(n) равно наименьшему числу m, такому что m! без остатка делится на n.  
Определим функцию S(M, N) = ∑s(n) для всех n ∈ [M, N]. К примеру, S(6, 10) = 3 + 7 + 4 + 6 + 5 = 25.

Найдите S(2100000, 2200000).