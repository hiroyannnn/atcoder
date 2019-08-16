n = input()
i = list(n)

r = 0
t = 0
c = 0
for a in i:
    c += 1
    r += t
    t = 0
    if c % 2 == 1:
        # 10 ** c -1 ~(10 ** c) - 1
        s = 10 ** (c - 1)
        e = 10 ** c
        t = len(range(s, e))
if c % 2 == 1:
    s = 10 ** (c - 1)
    e = int(n) + 1
    r += len(range(s, e))


print(r)
