"""
Lucky Numbers
Problem Description
A lucky number is a number which has exactly 2 distinct prime divisors. You are given a number A and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).  


Problem Constraints
1 <= A <= 5000


Input Format
The first and only argument is an integer A.


Output Format
Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.


Example Input
Input 1:
 A = 8
Input 2:
 12
 


Example Output
Output 1:
 1
Output 2:
 3
 


Example Explanation
Explanation 1:
 Between [1, 8] there is only 1 lucky number i.e 6.
 6 has 2 distinct prime factors i.e 2 and 3.
Explanation 2:
 Between [1, 12] there are 3 lucky number: 6, 10 and 12.
"""
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        spf=[i for i in range(n+1)]
        prime = [True for i in range(n+1)]
        def SieveOfEratosthenes(n):
            p = 2
            while (p * p <= n): 
                if (prime[p] == True): 
                    for i in range(p * p, n+1, p): 
                        prime[i] = False
                        if(spf[i]==i):
                            spf[i]=p
                p += 1
            return [p for p in range(2,n) if prime[p]==True]
        primes=SieveOfEratosthenes(n)
        ans=0
        def is_lucky(i):
            if prime[i]==True:
                return False
            mem=set()
            mem.add(spf[i])
            t=spf[i]
            while(i>1):
                i=i//t
                if(i==1):
                    break
                mem.add(spf[i])
                #print(mem)
                t=spf[i]
                if(len(mem)>2):
                    return False
            return len(mem)==2
                
        for i in range(6,n+1):
            t=is_lucky(i)
            #print(i,spf[i])
            #print(i,t)
            if(t):
                ans+=1
        return ans
        
        
                
