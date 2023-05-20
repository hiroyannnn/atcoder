import itertools

n = input()
list_ = [int(i) for i in input().split()]


def calc(x, y, z):
    if x < y + z:
        if y < x + z:
            if z < y + x:
                return 1
    return 0

# def range_calc():


sum = 0
for i in itertools.combinations(list_, r=3):
    sum += calc(*i)

print(sum)
