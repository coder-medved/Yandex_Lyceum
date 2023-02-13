from Samples.mapapi_PG import show_map


ml = {
    "Москва": ("ll=37.617698,55.755864&spn=0.2,0.2&pt=37.560106,55.791677,pmwtm1~37.440410,55.818023,pmwtm2~37.553820,55.715992,pmwtm3", "map")
}
for ml, mt in ml.values():
    show_map(ml, mt)

