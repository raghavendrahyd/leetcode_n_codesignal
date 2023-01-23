def solution(matrix):
    
    rowCount = len(matrix)
    colCount = len(matrix[0])
        
    res = {}
    for i in range(rowCount):
        for j in range(colCount):
            lbound_r = max(i-1,0)
            ubound_r = min(i+1,rowCount)
            lbound_c = max(j-1,0)
            ubound_c = min(j+1,colCount)

            tmp = [l for p in matrix[lbound_r:ubound_r+1] for l in p[lbound_c:ubound_c+1]]
            if (i) in res.keys(): 
                res[i].append(sum(tmp)-matrix[i][j])
            else:
                res[i] = [sum(tmp)-matrix[i][j]]
    return list(res.values())