def solution(s1, s2):
    def elem_count(str1):
        dict1 = {}
        for i in str1:
            if i in dict1: 
                dict1[i] += 1
            else:
                dict1[i] = 1

        return dict1
    
    dict_s1 = elem_count(s1)
    dict_s2 = elem_count(s2)
    
    s = 0
    for i in dict_s1:
        if i in dict_s2: s += min(dict_s1[i],dict_s2[i])
    return s