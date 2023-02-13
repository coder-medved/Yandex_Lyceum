from Samples.geocoder import geocode


def gc(address):
    toponym = geocode(address)
    if not toponym:
        return None, None
    tc = toponym["Point"]["pos"]
    tl, tll = tc.split(" ")
    return float(tl), float(tll)


try:
    ls = []
    ct = input().split(", ")
    for i in ct:
        crt = gc(i)[1]
        ls.append(crt)
    sc = ls.index(min(ls))
    print(ct[sc])
except TypeError:
    print("Некорректный ввод города")
