import sys
a = [int(i) for i in input().split()]
N = a[0]
K = a[1]

if K == 1:
    print(0)
    sys.exit()


def resZ(i, K):
    return abs(i - K)

ab = resZ(N, K)
# print(ab)
if N < ab:
    print(N)
    # print('end')
    sys.exit()

N = N % K
while True:
    ab = resZ(N, K)
    # print(ab)
    if N < ab:
        print(N)
        # print('end')
        sys.exit()

    N = ab
# def
