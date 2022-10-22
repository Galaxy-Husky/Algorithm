x, y = map(int, input().split())
if x == y:
    print('No Answer')
else:
    a = x * y
    b = x + y
    c = abs(y - x)
    z = []
    for i in range(a//b+1, a//c+1):
        if i != x and i != y:
            z.append(i)
    print(sorted(z, reverse=True))
