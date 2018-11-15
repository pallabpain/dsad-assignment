"""
Problem 3: Give an algorithm to traverse a binary tree in Zig Zag order.

Algorithm ZigZagTraversal(root)
1. Initialize two stacks currLevel, nextLevel
2. Set leftToRight flag to True
3. Push root into currLevel
4. Repeat steps 5-6 until currLevel is not empty
5. Pop a node from currLevel into a temp object and print it
6. If leftToRight is True, then
    a. Push the left child on nextLevel first,
    b. Then push the right child of the temp node.
7. Else if leftToRight is not True,
    a. Push the right child on nextLevel first,
    b. Then push the left child of the temp node.
8. If curreLevel is empty,
    a. leftToRight = ~leftToRight
    b. Swap the stacks currLevel and nextLevel
"""
from __future__ import print_function


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "[{0}<-{1}->{2}]".format(self.left, self.value, self.right)


def zig_zag_traversal(root):
    if root is None:
        return

    current_level = []
    next_level = []
    left_to_right = True
    current_level.append(root)

    while current_level:
        node = current_level.pop()
        print(node.value, " ", end="")
        if left_to_right:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        else:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
        if not current_level:
            left_to_right = not left_to_right
            current_level, next_level = next_level, current_level


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    zig_zag_traversal(root)
