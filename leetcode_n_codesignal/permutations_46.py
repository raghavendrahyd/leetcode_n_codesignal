def permute(nums: List[int]) -> List[List[int]]:
    A = nums[:]
    res=[]

    if (len(A)==1):
        return [A[:]]

    for i in range(len(A)):
        n = A.pop(0)

        perms = permute(A)

        for perm in perms:
            perm.append(n)

        res.extend(perms)
        A.append(n)
    return res