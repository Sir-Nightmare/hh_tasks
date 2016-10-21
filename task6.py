# Рассмотрим все возможные числа ab для 1<a<6 и 1<b<6:
# 22=4, 23=8, 24=16, 25=32 32=9, 33=27, 34=81, 35=243 42=16, 43=64, 44=256, 45=1024, 52=25, 53=125, 54=625, 55=3125
# Если убрать повторения, то получим 15 различных чисел.
#
# Сколько различных чисел ab для 2<a<128 и 2<b<116?

# Ответ: 13661
result = []
for a in range(3, 107):
    for b in range(3, 126):
        print(a, b)
        result.append(a ** b)
print(len(result))
result = set(result)
print(len(result))
