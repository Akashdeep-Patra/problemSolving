"""
Factorial Array
Problem Description
Groot has an array A of size N. Boring right? Groot thought so too, so he decided to construct another array B of the same size and defined elements of B as: B[i] = factorial of A[i] for every i such that 1<= i <= N.    
factorial of a number X denotes (1 x 2 x 3 x 4......(X-1) x (X)).
 Now Groot is interested in the total number of non-empty subsequences of array B such that every element in the subsequence has the same non empty set of prime factors. Since the number can be very large, return it modulo 109 + 7. NOTE: A set is a data structure having only distinct elements. Eg : the set of prime factors of Y=12 will be {2,3} and not {2,2,3}    


Problem Constraints
1 <= N <= 105
1 <= A[i] <= 106
Your code will run against a maximum of 5 test cases.


Input Format
Only argument is an integer array A of size N.


Output Format
Return an integer deonting the total number of non-empty subsequences of array B such that every element in the subsequence has the same set of prime factors modulo 109+7.


Example Input
Input 1:
 A = [2, 3, 2, 3]
Input 2:
 A = [2, 3, 4]
   


Example Output
Output 1:
 6
Output 2:
 4
   


Example Explanation
Explanation 1:
 Array B will be : [2, 6, 2, 6]
 The total possible subsequences are 6 : [2], [2], [2, 2], [6], [6], [6, 6].
Input 2:
 Array B will be : [2, 6, 24]
 The total possible subsequences are 4 : [2], [6], [24], [6, 24].



"""


from collections import Counter
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        n=max(a)
        prime=[True]*(n+1)
        spf=[x for x in range(n+1)]
        prime[0]=False
        prime[1]=False
        def seive(n):
            i=2
            while(i*i<=n):
                if(prime[i]==True):
                    for p in range(i*i,n+1,i):
                        prime[p]=False
                        if(spf[p]==p):
                            spf[p]=i
                i+=1
            return [x for x in range(n+1) if prime[x]==True]
        prime_bellow=seive(n)
        b=dict()
        last_prime=2
        b[2]=1
        b[1]=0
        b[0]=0
        def countall(n):
            c=b[2]
            for i in range(3,n+1):
                if(prime[i]==True):
                    c+=1
                    b[i]=c
                else:
                    b[i]=c
        countall(n)
        def count(n):
            return b[n]
        def power(x, y):
            if(y == 0): return 1
            temp = power(x, int(y / 2))  
              
            if (y % 2 == 0): 
                return temp * temp 
            else: 
                if(y > 0): return x * temp * temp 
                else: return (temp * temp) / x
        d=dict(Counter(list(map(count,a))))
        ans=0
        #print(b)
        for j,i in d.items():
            if(j!=0):
                ans+=(power(2,i)-1)
        
        return ans
