from functools import reduce

with open("input") as f:
    _ = f.read().removesuffix("\n").split("\n")

    def prio(c):
        return c - 97 + 1 if ord("a") <= c <= ord("z") else c - 65 + 26 + 1

    __ = map(
        prio,
        reduce(
            lambda a, x: a + x,
            map(
                lambda v: list(v[0].intersection(v[1])),
                map(
                    lambda v: (set(v[: len(v) // 2]), set(v[len(v) // 2 :])),
                    map(lambda v: [ord(c) for c in v], _),
                ),
            ),
        ),
    )
    print(sum(__))

    ___ = map(
        prio,
        map(
            ord,
            reduce(
                lambda a, x: a + x,
                map(
                    lambda v: list(v[0].intersection(v[1], v[2])),
                    map(
                        lambda v: list(map(set, v)),
                        [_[n : n + 3] for n in range(0, len(_), 3)],
                    ),
                ),
            ),
        ),
    )
    print(sum(___))
