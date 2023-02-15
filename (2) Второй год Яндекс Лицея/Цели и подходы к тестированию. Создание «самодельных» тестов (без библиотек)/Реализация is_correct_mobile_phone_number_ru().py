import sys


def is_correct_mobile_phone_number_ru():
    a = list(map(str.strip, sys.stdin))
    for lololoshka in a:
        lololoshka = "".join(lololoshka.split())
        if lololoshka.find("+7") != 0 and lololoshka.find("8") != 0:
            return "NO"
        if not all(lololoshka.split("-")):
            return "NO"
        else:
            lololoshka = lololoshka.replace("-", "")
        sb = lololoshka.find("(")
        eb = lololoshka.find(")")
        if sb > -1:
            if eb < sb or not lololoshka[sb + 1:eb].isdigit() \
                    or not lololoshka.count("(") == 1 or not lololoshka.count(")") == 1:
                return "NO"
        else:
            if eb > -1:
                return "NO"
        lololoshka = lololoshka.replace("(", "")
        lololoshka = lololoshka.replace(")", "")
        if lololoshka.find("8") == 0:
            lololoshka = "+7" + lololoshka[1:]
        if not lololoshka[1:].isdigit() or not len(lololoshka[1:]) == 11:
            return "NO"
        return "YES"


print(is_correct_mobile_phone_number_ru())