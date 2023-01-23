def solution(inputArray):
    max_1 = max(inputArray)
    for i in range(1,max_1+2):
        tmp_intersect = set(range(0,max_1+1,i)).intersection(inputArray)
        #print(i, set(range(0,max_1+1,i)), tmp_intersect)
        if len(tmp_intersect)>0:
            continue
        else:
            break
    
    return i        
