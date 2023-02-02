number = int(input())
a, b, c = number // 100, number // 10 % 10, number % 10
if a + b + c in (a * 3, b * 3, c * 3):
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')
