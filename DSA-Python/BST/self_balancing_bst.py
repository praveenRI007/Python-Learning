# Self-Balancing Binary Search Trees are height-balanced binary search trees that automatically keeps height as small as possible when insertion and deletion operations are performed on tree. The height is typically maintained in order of Log n so that all operations take O(Log n) time on average.
#
#
# How do Self-Balancing-Tree maintain height?
# A typical operation done by trees is rotation. Following are two basic operations that can be performed to re-balance a BST without violating the BST property (keys(left) < key(root) < keys(right)).
#
# Left Rotation
# Right Rotation
# T1, T2 and T3 are subtrees of the tree
# rooted with y (on the left side) or x (on
# the right side)
#      y                               x
#     / \     Right Rotation          /  \
#    x   T3   - - - - - - - >        T1   y
#   / \       < - - - - - - -            / \
#  T1  T2     Left Rotation            T2  T3
# Keys in both of the above trees follow the
# following order
#  keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
# So BST property is not violated anywhere.
#
#
# Examples: The most common examples of self-balancing binary search trees are
#
# AVL Tree
# Red Black Tree and
# Splay Tree


