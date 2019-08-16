from math import factorial

n = int(input())
l = [input() for i in range(n)]

res = []
for i in l:
    li = list(i)
    li.sort()
    res.append(''.join(li))

a = list(set(res))
t = 0
for i in a:
    r = res.count(i)
    if r == 2:
        t += 1
    elif r > 2:
        a = factorial(r) / factorial(2) / factorial(r - 2)
        t += a


print(t)
