"""
Problem: Give an algorithm for converting a tree to its mirror. Mirror of 
Algorithm ConvertToMirror(tree)
1. Call mirror for left-subtree
2. Call mirror for right sub-tree
3. Swap left and right sub-trees
    left, right = right, left
"""


class Node(object):
    """
    A node in a binary tree. Each node has an associated
    left pointer, right pointer and a value.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "[{0}<-{1}->{2}]".format(self.left, self.value, self.right)


class Tree(object):
    """
    A binary search tree where the value of the right child is
    greater than the parent's and that of the left child is lower
    than the parent's.
    """

    def __init__(self):
        self.root = None

    def insert_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        node = self.root
        while node is not None:
            if value < node.value:
                if node.left is None:
                    node.left = new_node
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = new_node
                    break
                node = node.right

    def __str__(self):
        return str(self.root)

    def mirror_tree(self):
        """
        Driver method for mirroring a tree
        """
        node = self.root
        self._mirror_tree(node)

    def _mirror_tree(self, node):
        """
        Mirrors a tree
        """
        if node is None:
            return
        self._mirror_tree(node.left)
        self._mirror_tree(node.right)
        node.left, node.right = node.right, node.left


if __name__ == "__main__":
    tree = Tree()
    tree.insert_node(10)
    tree.insert_node(5)
    tree.insert_node(15)
    tree.insert_node(3)
    tree.insert_node(4)
    tree.insert_node(25)
    tree.insert_node(12)
    tree.insert_node(24)
    tree.insert_node(26)
    tree.insert_node(9)
    print "Actual tree:"
    print tree
    tree.mirror_tree()
    print "\nMirrored tree:"
    print tree
