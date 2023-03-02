# Given two binary trees t1 and t2, determine whether
# the second tree is a subtree of the first tree.
# A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t.
# Determine whether or not there is a vertex v (possibly none) in tree t1
# such that a subtree for vertex v (possibly empty) in t1 equals t2


def solution(t1, t2):
    def is_identical(t1, t2):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        else:
            return (
                t1.value == t2.value
                and is_identical(t1.left, t2.left)
                and is_identical(t1.right, t2.right)
            )

    if t1 is None and t2 is None:
        return True
    if t1 is None:
        return False
    if t2 is None:
        return True
    if t1.value == t2.value:
        if is_identical(t1, t2):
            return True
    return solution(t1.left, t2) or solution(t1.right, t2)
