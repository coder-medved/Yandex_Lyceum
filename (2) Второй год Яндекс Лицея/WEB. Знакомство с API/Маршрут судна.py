from Samples.mapapi_PG import show_map


def sm():
    ml = {
        "Санкт-Петербург": (
        "ll=26.388038,59.916293&spn=2.5,2.5&pl=30.322803,59.944499,30.273800,59.952430,26.388038,59.916293,29.913396,59.891665",
        "map")
    }
    for ml, mt in ml.values():
        show_map(ml, mt)


sm()
