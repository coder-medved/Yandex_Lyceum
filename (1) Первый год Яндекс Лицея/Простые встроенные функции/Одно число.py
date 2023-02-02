a = float(input())
if abs(a) < 0.000001:
    print(1_000_000)
else:
    print(str(a ** -1))