from Samples.geocoder import geocode


def gac(address):
    toponym = geocode(address)
    pc = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
    return pc


pcc = gac("Москва, Петровки, 38")
print(f"Москва, Петровки, 38 имеет индекс: {pcc}")