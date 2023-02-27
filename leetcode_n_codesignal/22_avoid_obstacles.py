# Description:
#   You are given an array of integers representing coordinates of obstacles situated on a straight line.
#   Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.
#   Find the minimal length of the jump enough to avoid all the obstacles.
def solution(inputArray):
    max_1 = max(inputArray)
    for i in range(1, max_1 + 2):
        tmp_intersect = set(range(0, max_1 + 1, i)).intersection(inputArray)
        # print(i, set(range(0,max_1+1,i)), tmp_intersect)
        if len(tmp_intersect) > 0:
            continue
        else:
            break

    return i
