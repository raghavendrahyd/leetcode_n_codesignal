# Creating the TreeNode class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return self.value.__repr__()


# to add nodes like a binary search tree structure
def add(p: TreeNode, value) -> TreeNode:
    "add nodes like a binary search tree"
    if p is None:
        return TreeNode(value)
    if value < p.value:
        p.left = add(p.left, value)
    elif value > p.value:
        p.right = add(p.right, value)
    return p


# create a tree from a dictionary
def create_tree(t):
    """To create a tree from a dictionary
    Args:
        t (dict): dictionary with keys "value", "left", "right"
    Returns:
        TreeNode: root of the tree
    """
    if t is None:
        return None
    return TreeNode(
        t.get("value"), create_tree(t.get("left")), create_tree(t.get("right"))
    )


# get dictionary from the tree
def get_dict(t):
    if t is None:
        return None
    return {
        "value": t.value,
        "left": get_dict(t.left),
        "right": get_dict(t.right),
    }


# print tree with proper indentation from a tree node
def print_tree_node(t):
    """Prints the tree with correct indentation for each level"""

    def print_tree_helper(t, indent):
        if t is None:
            return
        print(indent + str(t.value))
        print_tree_helper(t.left, indent + "    ")
        print_tree_helper(t.right, indent + "    ")

    print_tree_helper(t, "")


# Getting the depth of the tree
def get_depth_tree(t):
    if t is None:
        return 0
    else:
        return 1 + max(get_depth_tree(t.left), get_depth_tree(t.right))


# get all vertices as a list from the tree
def get_all_vertices_tree(t):
    """ "
    Gets all vertices from the tree
    Args:
        t (TreeNode): root of the tree
    Returns:
        list: list of all vertices
    """
    if t is None:
        return []
    else:
        return (
            [t.value]
            + get_all_vertices_tree(t.left)
            + get_all_vertices_tree(t.right)
        )


def get_vertices_at_depth_tree(t, depth):
    """
    Gets vertices at a given depth
    Args:
        t (TreeNode): root of the tree
        depth (int): depth of the tree
    Returns:
        list: list of vertices at the given depth
    """
    if t is None:
        return []
    elif depth == 1:
        return [t.value]
    else:
        return get_vertices_at_depth_tree(
            t.left, depth - 1
        ) + get_vertices_at_depth_tree(t.right, depth - 1)


# Get sums of each root to leaf path
def get_sum_paths_from_tree(t):
    """
    Gets the sum of each root to leaf path
    Args:
        t (TreeNode): root of the tree
    Returns:
        list: list of sums of each root to leaf path
    """
    if t is None:
        return []
    elif t.left is None and t.right is None:
        return [t.value]
    else:
        return [t.value + i for i in get_sum_paths_from_tree(t.left)] + [
            t.value + i for i in get_sum_paths_from_tree(t.right)
        ]


# Some problem statements on Tree
# Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.
def is_mirror(t):
    if t is None:
        return True
    return is_mirror_helper(t.left, t.right)


def is_mirror_helper(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    else:
        return (
            t1.value == t2.value
            and is_mirror_helper(t1.left, t2.right)
            and is_mirror_helper(t1.right, t2.left)
        )


# Kth Smallest Element in a Binary Search Tree
def kth_smallest(root, k):
    def inorder(root):
        return (
            inorder(root.left) + [root.value] + inorder(root.right)
            if root
            else []
        )

    return inorder(root)[k - 1]


# find the lowest common ancestor of two nodes in a BST
# LCA is the lowest node in the tree that has both v1 and v2 as descendants
def lca(t, v1, v2):
    if t is None:
        return None
    if t.value == v1 or t.value == v2:
        return t.value
    elif t.value > v1 and t.value > v2:
        return lca(t.left, v1, v2)
    elif t.value < v1 and t.value < v2:
        return lca(t.right, v1, v2)
    else:
        return t.value


# check if one tree is a subtree of another
def is_subtree(t1, t2):
    """
    This function returns True if t2 is a subtree of t1
    """
    if t1 is None and t2 is None:
        return True
    if t1 is None:
        return False
    if t2 is None:
        return True
    if t1.value == t2.value:
        if is_identical(t1, t2):
            return True
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)


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


### Preorder Traversal and Inorder Traversal


# constructing a preorder traveral from a BST
# preorder traversal implies that the root is always the first element
# the next element is the root of the left subtree
# the last element is the root of the right subtree
def preorder(t):
    if t is None:
        return []
    return [t.value] + preorder(t.left) + preorder(t.right)


# constructing an inorder traveral from a BST
# inorder traversal implies that the root is always the middle element
# the first element is the root of the left subtree
# the last element is the root of the right subtree
def inorder(t):
    if t is None:
        return []
    return inorder(t.left) + [t.value] + inorder(t.right)


# construct a BST from a preorder and inorder traversal lists
def construct_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    root_index = inorder.index(
        preorder[0]
    )  # find the root in the inorder traversal
    root.left = construct_tree(
        preorder[1 : root_index + 1], inorder[:root_index]
    )  # construct the left subtree
    root.right = construct_tree(
        preorder[root_index + 1 :], inorder[root_index + 1 :]
    )  # construct the right subtree
    return root
