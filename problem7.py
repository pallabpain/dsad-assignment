"""
Given an array F with size n. Assume the array content F[i] indicates the length
of the ith file and we want to merge all these files into one single file. Check
whether the following algorithm gives the best solution for the problem or not?

Algorithm:
Merge files contiguously. That means, select the first two files and merge them.
Then select the output of the previous merge and merge with the third file and
keep doing so.

Note: Given two files A and B with size m and n, time complexity of merging is O(m + n)

Answer: This is a classic optimal merge pattern problem. The given algorithm is
one such pattern. But there is a better solution. 

1. Select the two smalled files from the list
2. Merge them
3. Repeat steps 1 and 2 until all files are merged
4. In the end, you get all the files merged in optimal cost.

Consider the following array F = [20, 30, 10, 5, 30]

With the given solution,
    1. 20 + 30 = 50
-> 50, 10, 5, 30
    2. 50 + 10 = 60
-> 60, 5, 30
    3. 60 + 5 = 65
-> 65, 30
    4. 65 + 30 = 95
Total Cost = 50 + 60 + 65 + 95 = 270

With the optimal solution,
    5, 10, 20, 30, 30

    1. 5 + 10 = 15
-> 15, 20, 30, 30
    2. 15 + 20 = 35
-> 30, 30, 35
    3. 30 + 30 = 60
-> 35, 60
    4. 35 + 60 = 95
Total Cost = 15 + 35 + 60 + 95 = 205

Using the optimal solution, we are getting 205 as the total cost as compared
with 270 using the given algorithm in the question.
"""

from __future__ import print_function


def simple_merge(F):
    n = len(F)
    total_cost = 0
    for _ in range(n - 1):
        f1 = F.pop(0)
        f2 = F.pop(0)
        cost = f1 + f2
        total_cost += cost
        F.insert(0, cost)
    return total_cost


def optimal_two_way_merge(F):
    n = len(F)
    total_cost = 0
    for _ in range(n - 1):
        # Get first min
        f1 = min(F)
        F.remove(f1)
        # Get second min
        f2 = min(F)
        F.remove(f2)
        # Merge them
        cost = f1 + f2
        total_cost += cost
        F.insert(0, cost)
    return total_cost


if __name__ == "__main__":
    F = [20, 30, 10, 5, 30]
    print("List of files = {}".format(F))
    cost = simple_merge(list(F))
    print("Cost with simple merge: {}".format(cost))
    cost = optimal_two_way_merge(list(F))
    print("Cost with optimal merge: {}".format(cost))

"""
Ouptut:

List of files = [20, 30, 10, 5, 30]
Cost with simple merge: 270
Cost with optimal merge: 205
"""
