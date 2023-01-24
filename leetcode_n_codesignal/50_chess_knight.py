def solution(cell):
    dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    def validmove(k,l):
        return (97<=ord(str(k))<=97+7) and (1<=l<=8)
    
    cell_x,cell_y =cell[0], int(cell[1])
    cnt=0
    for i in [ord(cell_x)-2,ord(cell_x)+2]:
        for j in [cell_y+1,cell_y-1]:
            #print(chr(i),j,validmove(chr(i),j))
            cnt +=validmove(chr(i),j)

    for i in [ord(cell_x)-1,ord(cell_x)+1]:
        for j in [cell_y+2,cell_y-2]:
            #print(chr(i),j,validmove(chr(i),j))
            cnt +=validmove(chr(i),j)
    return cnt
