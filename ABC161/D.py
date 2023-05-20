import sys
a = int(input())


def isLun(n):
    n = [int(i) for i in list(str(n))]
    a = n[0]
    if len(n) > 1:
        for i in n:
            b = abs(a - i)

            if b > 1:
                return False
            a = i
    return True


if a < 10:
    print(a)
    sys.exit()

res = 0
count = 9
i = 9

a -= 9

while count < a:
    i += 1
    if isLun(i):
        count += 1
        res = i
        # res.append(str(i + 1))
print(res)
