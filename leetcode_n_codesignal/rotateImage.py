# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).


def rotateImage(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    for i in a:
        i.reverse()
    return a
