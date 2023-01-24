def solution(bishop, pawn):
    dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    
    x1 = dict1[bishop[0]]
    y1 = int(bishop[1])
    x2 = dict1[pawn[0]]
    y2 = int(pawn[1])
    print(x1, y1, x2, y2)
    return ((x1-x2) == (y1-y2) or (x1-x2) == -1* (y1-y2))
