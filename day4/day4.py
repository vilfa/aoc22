with open("input") as f:
    _ = list(
        map(
            lambda v: (
                {x for x in range(v[0][0], v[0][1] + 1)},
                {x for x in range(v[1][0], v[1][1] + 1)},
            ),
            map(
                lambda v: (
                    list(map(int, v[0].split("-"))),
                    list(map(int, v[1].split("-"))),
                ),
                map(lambda v: v.split(","), f.read().removesuffix("\n").split("\n")),
            ),
        )
    )
    print(sum(map(lambda v: v[0].issubset(v[1]) or v[1].issubset(v[0]), _)))
    print(sum(map(lambda v: len(v[0].intersection(v[1])) > 0, _)))
