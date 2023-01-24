def solution(grid):
    arr = numpy.array(grid)
    for i in range(9):
        if not numpy.array_equal(numpy.sort(arr[i,:]),numpy.arange(1,10)): return False
        if not numpy.array_equal(numpy.sort(arr[:,i]),numpy.arange(1,10)): return False
        if not numpy.array_equal(numpy.sort(arr[int(i/3)*3:(int(i/3)*3)+3,((i-(int(i/3)*3))*3):((i-(int(i/3)*3))*3)+3].reshape(1,-1))[0],numpy.arange(1,10)): return False
    return True