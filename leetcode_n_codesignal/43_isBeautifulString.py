def solution(inputString):
    dict1 = {}
    for i in inputString:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i] = 1
    
    dict2 = sorted(dict1.items())
    print(dict2)
    dict2_vals = [i[1] for i in dict2]
    dict2_keys = [i[0] for i in dict2]
    
    if 'a' not in dict2_keys: return False
    for i in range(len(dict2_keys)-1):
       if ord(dict2_keys[i+1])-ord(dict2_keys[i]) != 1: return False
        
    print(dict2_vals,list(dict2_vals),sorted(dict2_vals, reverse=True))
    return sorted(dict2_vals, reverse=True)==list(dict2_vals) 