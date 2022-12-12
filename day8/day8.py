from functools import reduce
import sys

with open("input__") as f:
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

            print(list(zip(_sa, _st)))
            _stw = tuple(min(d + 1, fd) for fd, d in zip(_sa, _st))
            print(_stw)
            _stwf = _stw[0] * _stw[1] * _stw[2] * _stw[3]
            _w = max(_w, _stwf)


print(_v)
print(_w)
