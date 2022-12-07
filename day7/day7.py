from enum import Enum
import sys

with open("input") as f:
    _ = f.read().removesuffix("\n").split("\n")

    class nt(Enum):
        Dir = 0
        File = 1
        Root = 2

    class node:
        def __init__(self, type, name=None, size=0):
            self.type = type
            self.name = name
            self.size = size
            self._p = None
            self._d = 0
            self._c = dict()

        def __repr__(self):
            return f"- {self.type} {self.name} {self.size}"

        def __str__(self):
            _ = self._d * "|  " + f"- {self.type} {self.name} {self.size}\n"
            for __c in sorted(
                self._c.values(), key=lambda _v: _v.type.value, reverse=True
            ):
                _ += __c.__str__()
            return _

        def set_parent(self, parent):
            self._p = parent
            self._d = self._p._d + 1

        def add(self, type, name, size=0):
            self._c[name] = node(type, name, size)
            self._c[name].set_parent(self)

        def get(self, name):
            return self._c[name]

        def dirs(self, size_lim=sys.maxsize, cmp_fn=lambda siz, lim: siz < lim, rlvl=0):
            _ds = []
            _ssiz = self.siz()
            if cmp_fn(_ssiz, size_lim) and rlvl == 0:
                _ds.append((self, _ssiz))
            for _d in self._c.values():
                if _d.type == nt.Dir:
                    _siz = _d.siz()
                    if cmp_fn(_siz, size_lim):
                        _ds.append((_d, _siz))
                    _ds += _d.dirs(size_lim, cmp_fn, rlvl + 1)
            return _ds

        def siz(self):
            _siz = 0
            for _dent in self._c.values():
                if _dent.type == nt.File:
                    _siz += _dent.size
                elif _dent.type == nt.Dir:
                    _siz += _dent.siz()
            return _siz

    root = node(nt.Root, "")
    curr = root
    for i, ln in enumerate(_):
        if ln.startswith("$"):
            _ = ln.split(" ")[1:]
            if _[0] == "cd":
                if i != 0:
                    if _[1] == "..":
                        curr = curr._p
                    else:
                        curr = curr.get(_[1])
                else:
                    curr.name = _[1]
            elif _[0] == "ls":
                continue
        else:
            _ = ln.split(" ")
            if _[0] == "dir":
                curr.add(nt.Dir, _[1])
            elif _[0].isnumeric():
                curr.add(nt.File, _[1], int(_[0]))

    print(root)
    dirs = sorted(root.dirs(100000), key=lambda _k: _k[1])
    for _d in dirs:
        print(_d.__repr__())
    print(sum(map(lambda v: v[1], dirs)))

    disk_size = 70000000
    disk_rfree = 30000000
    disk_used = root.siz()
    disk_rdiff = disk_rfree - (disk_size - disk_used)

    print(
        "size", disk_size, "used", disk_used, "rfree", disk_rfree, "rdiff", disk_rdiff
    )

    appr_dirs = sorted(
        root.dirs(disk_rdiff, lambda siz, lim: siz >= lim), key=lambda _k: _k[1]
    )
    for _d in appr_dirs:
        print(_d.__repr__())
    print(sum(map(lambda v: v[1], appr_dirs)))
