import sys
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
b = sorted(b, reverse=True)
# b.reverse()
# list2 = sorted(list1, reverse=True)


def canSelect(a, total, M):
    return a >= total / (4 * M)


def returnWord(flag):
    if flag:
        return 'Yes'
    return 'No'


total = sum(b)
M = a[1]
count = 0
res = 'Yes'
for i in b:
    count += 1
    if not canSelect(i, total, M):
        res = returnWord(False)
    if count == M:
        print(res)
        sys.exit()

# print(-(-a[0] // a[1]))
