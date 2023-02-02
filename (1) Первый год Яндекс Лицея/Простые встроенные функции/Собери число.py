a = int(input())
b = ((a // 100) + (a // 10) % 10)
c = (((a // 10) % 10) + (a % 100) % 10)
if b > c:
    print(str(b) + str(c))
else:
    print(str(c) + str(b))
