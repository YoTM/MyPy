
with open("data.txt") as d, open("result.txt", "w") as res:
    x = d.read()
    lines = x.splitlines()
    lines.reverse()
    res.write("\n".join(lines))
