from Samples.geocoder import geocode


def gac(address):
    toponym = geocode(address)
    tc = toponym["Point"]["pos"]
    return tc


lst = ["Москва, Красная площадь, 1"]
for i in lst:
    cc = gac(i)
    print(f"{i} имеет координаты: {cc}")
print("")