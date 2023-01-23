def solution(inputString):
    s_list = inputString.split(".")
    if len(s_list) != 4: return False
    
    cnt = 0
    for i in s_list:
        if i !="" and i !=" " and i.isnumeric():
            if str(int(i))==i and int(i)>=0 and int(i)<=255:
                cnt +=1
    if cnt ==4: return True
    return False