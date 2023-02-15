from yandex_testing_lesson import is_correct_mobile_phone_number_ru


def test_is_correct_mobile_phone_number_ru():
    tk = (
        ("+79044513880", True),
        ("89044513880", True),
        ("8(904)4513880", True),
        ("8 904 451-38-80", True),
        ("+7 904 451 38-80", True),
        ("890445138880", False),
        ("89(044513880", False),
        ("8)9044513880", False),
        ("870445(3880", False),
        ("590444513880", False),
    )
    for inp, cos in tk:
        if is_correct_mobile_phone_number_ru(inp) != cos:
            return False
    return True


if not test_is_correct_mobile_phone_number_ru():
    print('NO')
else:
    print('YES')