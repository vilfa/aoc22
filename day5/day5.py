import re

with open("input") as f:
    _ = f.read().removesuffix("\n").split("\n")

    ns = sum(
        map(
            lambda v: len(re.sub("  +", ",", v).split(",")),
            filter(lambda v: re.sub(" +", "", v).isnumeric(), _),
        )
    )
    st = list(
        map(
            lambda v: [v[n : n + 4].strip() for n in range(0, len(v), 4)],
            filter(lambda v: "[" in v and "]" in v, _),
        )
    )
    mv = map(
        lambda v: (int(v[1]), int(v[3]), int(v[5])),
        map(lambda v: v.split(" "), filter(lambda v: "move" in v, _)),
    )

    ws = {i + 1: [] for i in range(ns)}
    for r in st:
        for j, e in enumerate(r):
            if e != "":
                ws[j + 1].append(e)

    for k, v in ws.items():
        v = v.reverse()

    def move(w: dict[int, list], m: tuple[int, int, int]):
        nc, fr, to = m
        if nc > 1:
            move_m(w, m)
            return
        for _ in range(nc):
            if len(w[fr]):
                w[to].append(w[fr].pop())

    def move_m(w: dict[int, list], m: tuple[int, int, int]):
        nc, fr, to = m
        c = w[fr][-nc:]
        del w[fr][-nc:]
        w[to] += c

    for m in mv:
        move(ws, m)

    print(list(map(lambda v: v[-1], ws.values())))
