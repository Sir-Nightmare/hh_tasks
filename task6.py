result = []
for a in range(3, 107):
    for b in range(3, 126):
        print(a, b)
        result.append(a ** b)
print(len(result))
result = set(result)
print(len(result))
