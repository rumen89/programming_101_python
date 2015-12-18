a = '2x^2 + 3x + 4'
b = []
c = a.split()
for item in c:
    if item != '+' and item != '-':
        b.append(item)

print(b)
