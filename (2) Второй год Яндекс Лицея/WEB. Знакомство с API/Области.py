from Samples.geocoder import geocode


def gac(town, component_index):
    toponym = geocode(town)
    pc = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
    return pc[component_index]["name"]


lst = ["Барнаул", "Мелеуз", "Йошкар-Ола"]
for i in lst:
    pcc = gac(i, 2)
    print(f"{i}: {pcc}")
print("")
