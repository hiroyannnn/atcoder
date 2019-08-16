a = input().split()

n = int(a[0])
m = int(a[1])

a1 = m - (n - 1)
a2 = m + (n)

max = 1000000
min = -1000000

if a1 < min:
    a1 = min
if a2 > max:
    a2 = max

l = map(str, range(a1, a2))
print(' '.join(l))
