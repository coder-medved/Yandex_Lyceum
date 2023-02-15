def is_prime(n):
    if n <= 2:
        return n == 2
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


n = int(input())
if is_prime(n):
    print("YES")
else:
    print("NO")