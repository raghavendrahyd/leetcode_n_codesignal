#  Given a rectangular matrix of characters, add a border of asterisks(*) to it.
def solution(picture):
    rows = len(picture)
    cols = len(picture[0]) + 2
    res = [0] * (rows + 2)
    res[0] = "".join(["*"] * cols)
    res[rows + 1] = res[0]
    for i in range(1, rows + 1):
        res[i] = "*" + picture[i - 1] + "*"
    return res
