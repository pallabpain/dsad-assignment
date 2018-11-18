"""
Given two BSTs, check whether the elements of them are the same or not.
For example, two BSTs with data 10, 5, 20, 15, 30 and 10, 20, 15, 30, 5
should return true and the dataset with 10, 5, 20, 15, 30 and 10, 5, 30, 20, 5
should return false.

Note: BST data can be in any order

Algorithm CompareBSTs(bstA bstB)
1. Initialize two empty arrays of size equal to total elements in each BST,
   elementsA, elementsB
2. Perform inorder traversal on the BSTs and store the result in the arrays
   initialized in step 1.
3. Compare elementsA and elementsB, if equal then BSTs are equal, else BSTs
   are not equal
"""

from __future__ import print_function


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self, *args):
        self.root = None
        if args:
            for arg in args:
                self.insert_node(arg)

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

    def get_sorted_list(self):
        elements = []
        self._inorder(self.root, elements)
        return elements

    def _inorder(self, node, elements):
        if node is None:
            return
        self._inorder(node.left, elements)
        elements.append(node.value)
        self._inorder(node.right, elements)

    def __eq__(self, other):
        self_list = self.get_sorted_list()
        other_list = other.get_sorted_list()
        return self_list == other_list


if __name__ == "__main__":

    bstA = BinarySearchTree(10, 5, 20, 15, 30)
    bstB = BinarySearchTree(10, 20, 15, 30, 5)

    print("Are bstA and bstB equal? {}".format(bstA == bstB))

    bstC = BinarySearchTree(10, 5, 20, 15, 30)
    bstD = BinarySearchTree(10, 5, 30, 20, 5)

    print("Are bstC and bstD equal? {}".format(bstC == bstD))

"""
Output:

Are bstA and bstB equal? True
Are bstC and bstD equal? False
"""