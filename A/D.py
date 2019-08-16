n = input()
print(n)
count = []
for _ in range(len(n)):
    count.append(1)

#10 ** 100


def ido(l, n):
    for i in range(len(n)):

        if n[i] == 'R':
            l[i] -= 1
            l[i + 1] += 1

        else:
            l[i] -= 1
            l[i - 1] += 1
    return l


m = 10 ** 3
i = 0
while i < m:
    count = ido(count, n)
    i += 1
    print(count)

print(count)
