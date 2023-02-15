from yandex_testing_lesson import is_prime


def test_is_prime():
    test_cases = (
        ('not a number', None),
        (-1, None),
        (0, None),
        (1, None),
        (2, True),
        (3, True),
        (6, False),
        (7, True),
        (9, False),
        (16, False)
    )
    for in_n, correct_answer in test_cases:
        try:
            answer = is_prime(in_n)
        except TypeError:
            if type(in_n) == int:
                return False
        except ValueError:
            if in_n > 1:
                return False
        else:
            if correct_answer != answer:
                return False
    return True


print('YES') if test_is_prime() else print('NO')