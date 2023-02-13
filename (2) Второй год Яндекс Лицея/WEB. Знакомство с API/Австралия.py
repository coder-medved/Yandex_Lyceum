from Samples.mapapi_PG import show_map


def sm():
    ml = {
        "Австралия": ("ll=135.746181,-27.483765&spn=20,20", "sat")
    }
    for ml, mt in ml.values():
        show_map(ml, mt)


sm()
