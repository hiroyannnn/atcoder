a = input().split()

n = int(a[0])
m = int(a[1])

l = [0, 0, 0]
l[0] = n + m
l[1] = n - m
l[2] = n * m

print(max(l))
