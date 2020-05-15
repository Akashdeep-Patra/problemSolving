"""
Sorted Permutation Rank with Repeats
Problem Description
Given a string A, find the rank of the string amongst its permutations sorted lexicographically. Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations. Look at the example for more details. NOTE:   
The answer might not fit in an integer, so return your answer % 1000003 where 1000003 is a prime number.
String A can consist of both lowercase and uppercase letters. Characters with lesser ascii value are considered smaller i.e. 'a' > 'Z'.
    


Problem Constraints
1 <= len(A) <= 1000000


Input Format
First argument is a string A.


Output Format
Return an integer denoting the rank.


Example Input
Input 1:
 A = "aba"
Input 2:
 A = "bca"
   


Example Output
Output 1:
 2
Output 2:
 4
   


Example Explanation
Explanation 1:
 The order permutations with letters 'a', 'a', and 'b' :
    aab
    aba 
    baa
 So, the rank is 2.
Explanation 2:
 The order permutations with letters 'a', 'b', and 'c' :
    abc
    acb 
    bac
    bca
    cab
    cba
 So, the rank is 4.
"""
from collections import defaultdict
class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
	    def fact(n):
	        p=1
	        for i in range(2,n+1):
	            p = p*i
	        return p
	    
	    count_max = [0]*len(A)
	    
	    def right_max(count_max,A):
	        for i in range(len(A)-1):
	            for j in range(i+1,len(A)):
	                if A[j]<A[i]:
	                    count_max[i] += 1
	                    
	    right_max(count_max,A)
	    l = len(A)
	    f_fact = fact(l-1)
	    
	    rank = 0
	    
	    for i in range(l-1):
	        duplicates = defaultdict(int)
	        for j in range(i,l):
	            duplicates[A[j]] += 1
	        exp = count_max[i]*f_fact
	        for value in duplicates.values():
	            if value>1:
	                exp = exp//fact(value)
	        rank += exp
	        f_fact = f_fact//(l-i-1)
	        
	    rank += (count_max[-1])
	   
	    return (rank+1)%1000003
