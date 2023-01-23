def solution(a):
        len_a = len(a)
        tree_idxs = []
        main_elems =[]
        
        for i in range(len_a):
            if a[i]==-1:
                tree_idxs.append(i)
            else:
                main_elems.append(a[i])
        
        main_elems=sorted(main_elems)
        
        b=[]
        for i in range(len_a):
            if i in tree_idxs:
                b.append(-1)
            else:
                b.append(main_elems[0])
                main_elems.pop(0)
        
        return b