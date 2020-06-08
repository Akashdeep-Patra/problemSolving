class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        first_smallest_left=[0]*len(a)
        first_smallest_right=[0]*len(a)
        first_greater_left=[0]*len(a)
        first_greater_right=[0]*len(a)
        stack=[]
        mod=10**9+7
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
	    stack=[]
	    for i in range(len(a)):
	        while(len(stack)!=0 and a[stack[-1]]<=a[i]):
	            stack.pop()
	        if(len(stack)==0):
	            first_greater_left[i]=-1
	            stack.append(i)
	        else:
	            first_greater_left[i]=stack[-1]
	            stack.append(i)
	    stack=[]
	    for i in range(len(a))[::-1]:
	        while(len(stack)!=0 and a[stack[-1]]<=a[i]):
	            stack.pop()
	        if(len(stack)==0):
	            first_greater_right[i]=len(a)
	            stack.append(i)
	        else:
	            first_greater_right[i]=stack[-1]
	            stack.append(i)
	    ans=0
	    for i in range(len(a)):
	        ans=(ans-a[i]*(first_smallest_right[i]-i)*(i-first_smallest_left[i]))%mod
	        ans=(ans+a[i]*(first_greater_right[i]-i)*(i-first_greater_left[i]))%mod
	   # print(first_smallest_left)
	   # print(first_smallest_right)
	   # print(first_greater_left)
	   # print(first_greater_right)
	    return ans
"""
MAX and MIN
Problem Description

Given an array of integers A .

value of a array = max(array) - min(array).

Calculate and return the sum of values of all possible subarrays of A % 109+7.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 1000000



Input Format
The first and only argument given is the integer array A.



Output Format
Return the sum of values of all possible subarrays of A % 10^9+7.



Example Input
Input 1:

 A = [1]
Input 2:

 A = [4, 7, 3, 8]


Example Output
Output 1:

 0
Output 2:

 26


Example Explanation
Explanation 1:

Only 1 subarray exists. Its value is 0.
Explanation 2:

value ( [4] ) = 4 - 4 = 0
value ( [7] ) = 7 - 7 = 0
value ( [3] ) = 3 - 3 = 0
value ( [8] ) = 8 - 8 = 0
value ( [4, 7] ) = 7 - 4 = 3
value ( [7, 3] ) = 7 - 3 = 4
value ( [3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3] ) = 7 - 3 = 4
value ( [7, 3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3, 8] ) = 8 - 3 = 5
sum of values % 10^9+7 = 26
"""