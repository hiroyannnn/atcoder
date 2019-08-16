import sys
n = input()
l = input().split()
num = -1
for a in reversed(l):
    if num == -1:
        num = int(a)
    else:
        if num >= int(a):
            num = int(a)
        elif num >= int(a) - 1:
            num = int(a) - 1
        else:
            print('No')
            sys.exit()
print('Yes')
