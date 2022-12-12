from functools import reduce
import sys

with open("input") as f:
    _ = f.read().removesuffix("\n").split("\n")
    G = [[int(tc) for tc in tr] for tr in _]
    _v = 4 * len(G) - 4
    _w = -1
    for i, tr in enumerate(G[1:-1], start=1):
        for j, tc in enumerate(tr[1:-1], start=1):
            w, e = tr[:j], tr[j + 1 :]
            n, s = [t[j] for t in G[:i]], [t[j] for t in G[i + 1 :]]
            _sa = (len(w), len(e), len(n), len(s))
            _st = (
                sum(map(lambda v: v < tc, w)),
                sum(map(lambda v: v < tc, e)),
                sum(map(lambda v: v < tc, n)),
                sum(map(lambda v: v < tc, s)),
            )
            _s = sum((e1 == e2 for e1, e2 in zip(_sa, _st)))
            _v += _s > 0

            w.reverse()
            n.reverse()

            def vdist(t, v):
                d = 0
                for e in v:
                    if e < t:
                        d += 1
                    elif e >= t:
                        d += 1
                        return d
                return d

            wv, ev, nv, sv = vdist(tc, w), vdist(tc, e), vdist(tc, n), vdist(tc, s)
            _stw = wv * ev * nv * sv
            _w = max(_w, _stw)


print(_v)
print(_w)
