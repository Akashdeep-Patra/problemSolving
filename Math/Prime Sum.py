"""
Prime Sum
Problem Description
Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to given number.   If there are more than one solutions possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
NOTE: A solution will always exist. Read Goldbach's conjecture.     


Problem Constraints
4 <= A <= 2*107


Input Format
First and only argument of input is an even number A.


Output Format
Return a integer array of size 2 containing primes whose sum will be equal to given number.


Example Input
 4


Example Output
 [2, 2]


Example Explanation
 There is only 1 solution for A = 4.

"""
class Solution:
    	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
	    def SieveOfEratosthenes(n):
            prime = [True for i in range(n+1)] 
            p = 2
            while (p * p <= n): 
                if (prime[p] == True): 
                    for i in range(p * p, n+1, p): 
                        prime[i] = False
                p += 1
            return set([p for p in range(2,n) if prime[p]==True])
        primes=SieveOfEratosthenes(A)
        for i in range(2,A):
            if i in primes and A-i in primes:
                return [i,A-i]
