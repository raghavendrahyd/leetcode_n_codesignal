# Leetcode 498
#   Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order.
#
def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    mat1 = mat
    m = len(mat1)
    if m == 0:
        return []
    n = len(mat1[0]) if m > 0 else 0
    dict_t = {}
    for i in range(m):
        for j in range(n):
            if (i + j) in dict_t.keys():
                dict_t[(i + j)].append([i, j])
            else:
                dict_t[(i + j)] = [[i, j]]

    list_req = []
    for k, v in dict_t.items():
        if k % 2 != 0:
            list_req.append(v)
        else:
            list_req.append(v[::-1])

    return [mat1[item[0]][item[1]] for sublist in list_req for item in sublist]
