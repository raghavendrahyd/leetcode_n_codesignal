# Given a binary tree t and an integer s, determine whether there is a root to leaf path in t
# such that the sum of vertex values equals s

# Example:

# For
# t = {
#     "value": 4,
#     "left": {
#         "value": 1,
#         "left": {
#             "value": -2,
#             "left": null,
#             "right": {
#                 "value": 3,
#                 "left": null,
#                 "right": null
#             }
#         },
#         "right": null
#     },
#     "right": {
#         "value": 3,
#         "left": {
#             "value": 1,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 2,
#             "left": {
#                 "value": -2,
#                 "left": null,
#                 "right": null
#             },
#             "right": {
#                 "value": -3,
#                 "left": null,
#                 "right": null
#             }
#         }
#     }
# }
# and s = 7, the output should be
# hasPathWithGivenSum(t, s) = true.


def solution(t, s):
    def get_sum_paths_from_tree(t):
        if t is None:
            return []
        elif t.left is None and t.right is None:
            return [t.value]
        else:
            return [t.value + i for i in get_sum_paths_from_tree(t.left)] + [
                t.value + i for i in get_sum_paths_from_tree(t.right)
            ]

    return s in get_sum_paths_from_tree(t)
