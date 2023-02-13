from Samples.geocoder import geocode


def gac(town, component_index):
    toponym = geocode(town)
    cmp = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
    return cmp[component_index]["name"]


lst = ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград"]
for i in lst:
    pc = gac(i, 1)
    print(f"{i}: {pc}")
print("")