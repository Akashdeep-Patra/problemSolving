def histogram(a):
    first_left_smaller = [0] * len(a)
    first_right_smaller = [0] * len(a)
    stack = []
    for i in range(len(a)):
        while (len(stack) != 0 and a[i] <= a[stack[-1]]):
            stack.pop()
        if (len(stack) == 0):
            first_left_smaller[i] = -1
            stack.append(i)
        else:
            first_left_smaller[i] = stack[-1]
            stack.append(i)
    stack = []
    for i in range(len(a))[::-1]:
        while (len(stack) != 0 and a[i] <= a[stack[-1]]):
            stack.pop()
        if (len(stack) == 0):
            first_right_smaller[i] = len(a)
            stack.append(i)
        else:
            first_right_smaller[i] = stack[-1]
            stack.append(i)
    ans = float("-inf")
    for i in range(len(a)):
        ans = max(ans,
                  a[i] * (first_right_smaller[i] - first_left_smaller[i] - 1))
    return ans


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, a):
        height_current = [0] * len(a[0])
        height_prev = [0] * len(a[0])
        ans = float("-inf")
        for i in range(len(a)):
            for j in range(len(a[0])):
                if (a[i][j] == 1):
                    height_current[j] = height_prev[j] + 1
                else:
                    height_current[j] = 0
            # print(height_current)
            height_prev = height_current[:]
            ans = max(ans, histogram(height_current))
        return ans


"""
Maximum Rectangle
Given a 2D binary matrix of integers A containing 0's and 1's of size N x M.

Find the largest rectangle containing only 1's and return its area.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.


Input Format

The only argument given is the integer matrix A.
Output Format

Return the area of the largest rectangle containing only 1's.
Constraints

1 <= N, M <= 1000
0 <= A[i] <= 1
For Example

Input 1:
    A = [   [0, 0, 1]
            [0, 1, 1]
            [1, 1, 1]   ]
Output 1:
    4

Input 2:
    A = [   [0, 1, 0, 1]
            [1, 0, 1, 0]    ]
Output 2:
    1
"""
