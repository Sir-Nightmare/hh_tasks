i = 1
while True:
    double = str(i * 2)
    triple = str(i * 3)
    if len(double) == len(triple):
        double = list(double)
        triple = list(triple)
        double.sort()
        triple.sort()
        double = ''.join(double)
        triple = ''.join(triple)
        if double == triple:
            print(i)
            break
    i += 1
