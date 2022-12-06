with open("input") as f:
    _ = f.read().removesuffix("\n")
    csd, msd = False, False
    for i in range(len(_)):
        cs = set(_[i : i + 4])
        ms = set(_[i : i + 14])
        if len(cs) == 4 and not csd:
            csd = True
            print(cs)
            print(i + 4)
        if len(ms) == 14 and not msd:
            msd = True
            print(ms)
            print(i + 14)
