with open("input") as f:
    _ = list(
        map(
            lambda v: sum(map(lambda v: int(v), v)),
            map(lambda v: v.split("\n"), f.read().removesuffix("\n").split("\n\n")),
        )
    )
    print(max(_), _.index(max(_)), f"({_.index(max(_)) + 1})")
    _ = dict(sorted({k: v for k, v in enumerate(_)}.items(), key=lambda i: i[1]))
    print(sum(list(_.values())[-3:]))
