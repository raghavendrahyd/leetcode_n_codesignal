# Description: Given an array of strings, return another array containing all of its longest strings.
def solution(inputArray):
    max_len = max([len(i) for i in inputArray])  # get max len first
    return [i for i in inputArray if len(i) == max_len]
