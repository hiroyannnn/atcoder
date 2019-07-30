arg = input().split()
n = int(arg[0])
total = int(arg[1])

count1k = 0
count5k = 0
count10k = 0
current = 0


def check(current, total):
    return current > total


def printResult(count10k, count5k, count1k):
    if count10k == 0 and count5k == 0 and count1k == 0:
        print(-1, -1, -1)
    else:
        print(count10k, count5k, count1k)


for i in range(n + 1):
    count10k = n - int(i)
    current += 100000 * n
    if check(current, total):
        if current == total:
            break

printResult(count10k, count5k, count1k)
