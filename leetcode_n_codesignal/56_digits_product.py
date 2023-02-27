# Description: Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product.
# If there is no such integer, return -1 instead.
#
def solution(product):
    def getDigits(num1):
        digits = []
        for divisor in range(9, 1, -1):
            while num1 % divisor == 0:
                num1 /= divisor
                digits.append(divisor)
        return digits, num1

    if product == 0:
        return 10
    if product == 1:
        return 1
    digits1, num2 = getDigits(product)
    if len(digits1) == 0:
        return -1
    if num2 > 1:
        return -1
    # return int("".join([str(i) for i in digits1[::-1]]))
    res = 0
    for i in range(len(digits1) - 1, -1, -1):
        res = 10 * res + digits1[i]
    return res
