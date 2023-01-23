def solution(inputString):
    dict1 = {}
    for i in inputString:
        if i in dict1: dict1[i] += 1
        else: dict1[i] = 1
    l1 = [k%2 for k in dict1.values()]
    return (min(l1)+max(l1)==0 and len(inputString)%2==0) or (sum(l1)==1 and len(inputString)%2 != 0)

