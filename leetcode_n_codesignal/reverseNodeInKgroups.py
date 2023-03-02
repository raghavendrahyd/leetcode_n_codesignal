# Given a linked list l, reverse its nodes k at a time and return the modified list.
# k is a positive integer that is less than or equal to the length of l.
# If the number of nodes in the linked list is not a multiple of k,
# then the nodes that are left out at the end should remain as-is.
# You may not alter the values in the nodes - only the nodes themselves can be changed.


def reverseNodesInKGroups(l, k):
    node = l
    a_vals = []
    while node:
        a_vals.append(node.value)
        node = node.next

    res = []
    sublist = []
    for idx, i in enumerate(a_vals):
        if idx % k:
            sublist.append(i)
        else:
            res.extend([sublist[::-1]])
            sublist = []
            sublist.append(i)
    res.extend([sublist[::-1]] if len(sublist) == k else [sublist])
    a_vals = [i for sublist in res for i in sublist]

    l = ListNode(a_vals[0])
    curr = l
    for i in range(1, len(a_vals)):
        curr.next = ListNode(a_vals[i])
        curr = curr.next
    return l
