class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, a):
	    first_smallest_left=[0]*len(a)
	    first_smallest_right=[0]*len(a)
	    stack=[]
	    for i in range(len(a)):
	        while(len(stack)!=0 and a[stack[-1]]>=a[i]):
	            stack.pop()
	        if(len(stack)==0):
	            first_smallest_left[i]=-1
	            stack.append(i)
	        else:
	            first_smallest_left[i]=stack[-1]
	            stack.append(i)
	    stack=[]
	    for i in range(len(a))[::-1]:
	        while(len(stack)!=0 and a[stack[-1]]>=a[i]):
	            stack.pop()
	        if(len(stack)==0):
	            first_smallest_right[i]=len(a)
	            stack.append(i)
	        else:
	            first_smallest_right[i]=stack[-1]
	            stack.append(i)
	    ans=float("-inf")
	    for i in range(len(a)):
	        ans=max(ans,a[i]*(first_smallest_right[i]-first_smallest_left[i]-1))
	   # print(first_smallest_left)
	   # print(first_smallest_right)
	    return ans


"""
Largest Rectangle in Histogram
Problem Description

Given an array of integers A .

A represents a histogram i.e A[i] denotes height of the ith histogram's bar. Width of each bar is 1.

Find the area of the largest rectangle formed by the histogram.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 1000000000



Input Format
The only argument given is the integer array A.



Output Format
Return the area of largest rectangle in the histogram.



Example Input
Input 1:

 A = [2, 1, 5, 6, 2, 3]
Input 2:

 A = [2]


Example Output
Output 1:

 10
Output 2:

 2


Example Explanation
Explanation 1:

The largest rectangle has area = 10 unit. Formed by A[3] to A[4].
Explanation 2:

Largest rectangle has area 2.
"""