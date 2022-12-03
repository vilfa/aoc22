with open("input") as f:
    # Part 1
    win = ["A 2", "B 3", "C 1"]
    loss = ["A 3", "B 1", "C 2"]
    tie = ["A 1", "B 2", "C 3"]
    _ = f.read().removesuffix("\n")
    __ = _.replace("X", "1").replace("Y", "2").replace("Z", "3")

    def f(v):
        if v in win:
            s = 6 + int(v.split(" ")[1])
        elif v in tie:
            s = 3 + int(v.split(" ")[1])
        else:
            s = int(v.split(" ")[1])
        return s

    __ = sum(map(f, __.split("\n")))
    print(__)

    # Part 2
    win = {"A": 2, "B": 3, "C": 1}
    loss = {"A": 3, "B": 1, "C": 2}
    tie = {"A": 1, "B": 2, "C": 3}
    pts = {"X": 0, "Y": 3, "Z": 6}

    def f(v):
        g = v.split(" ")
        match g[1]:
            case "X":
                return loss[g[0]] + pts[g[1]]
            case "Y":
                return tie[g[0]] + pts[g[1]]
            case "Z":
                return win[g[0]] + pts[g[1]]

    _ = sum(map(f, _.split("\n")))
    print(_)
