a = input()
b = list(input())

print(len([n for i, n in enumerate(b) if i == 0 or n != b[i-1]]))
