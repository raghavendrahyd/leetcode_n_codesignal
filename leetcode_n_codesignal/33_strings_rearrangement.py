# Description: Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that
# after the rearrangement the strings at consecutive positions would differ by exactly one character.


def solution(inputArray):
    def perms(b):
        a = b
        res = []
        if len(a) == 1:
            return [a[:]]
        for i in range(len(a)):
            d = a.pop(0)
            perms1 = perms(a)
            for p in perms1:
                p.append(d)

            res.extend(perms1)
            a.append(d)
        return res

    perms_res = perms(inputArray)

    lis = []
    for combo in perms_res:
        diff_l1 = []
        for i in range(1, len(combo)):
            diff_l1.append(
                sum([i != j for i, j in zip(combo[i], combo[i - 1])])
            )

        if [1] * (len(combo) - 1) == diff_l1:
            return True

    return False
