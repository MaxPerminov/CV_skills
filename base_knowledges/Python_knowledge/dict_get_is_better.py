# to dodge the error, it's better to use dict.get(key) instead of dict[key]
a = {1: "test"}
print(f"{a.get(0)},", a.get(1))
print(f"{a[0]},", a[1])
