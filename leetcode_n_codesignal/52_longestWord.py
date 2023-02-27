# Description: Given a string, find the longest word in it.
def solution(text):
    """Given a string, find the longest word in it."""
    lis = []
    word = ""
    for char in text:
        if char.isalpha():
            word += char
        else:
            lis.append(word)
            word = ""
    lis.append(word)

    res = lis[0]
    maxlen = len(lis[0])
    # print(res, maxlen, lis)
    for i in lis:
        if len(i) > maxlen:
            res = i
            maxlen = len(i)
    return res
