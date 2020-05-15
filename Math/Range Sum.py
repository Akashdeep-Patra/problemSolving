
"""
Range Sum
Problem Description
Given two integers A and B such that A <= B. A Function F is defined as follows:
F[0] = 0
F[1] = 1
F[n] = F[n-1] + F[n-2]; n > 1
Function S(A, B) = F[A] + F[A+1] + F[A+2] + ... + F[B]. Find and return S(A, B) modulo (109+7).  


Problem Constraints
0 <= A <= B <= 109


Input Format
The arguments given are two integers A and B.


Output Format
Return an integer denoting the value of S(A, B) modulo (109+7).


Example Input
Input 1:
 A = 0
 B = 3
Input 2:
 A = 3
 B = 4
 


Example Output
Output 1:
 4
Output 2:
 5
 


Example Explanation
Explanation 1:
 F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2.
 S(0, 3) = F(0) + F(1) + F(2) + F(3) = 0 + 1 + 1 + 2 = 4.
Explanation 2:
 F(3) = 2, F(4) = 3.
 S(3, 4) = F(3) + F(4) = 2 + 3 = 5.



"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        fib1=0
        fib2=1
        sum=0
        cache={}
        MOD=10**9+7
        def fib(n):
            #in logn time!
            if(n<2):
                return 1
            if(n in cache):
                return cache[n]
            cache[n]=(fib((n+1) // 2)*fib(n//2) + fib((n-1) // 2)*fib((n-2) // 2)) % MOD
            return cache[n]
            
        def sum_fib(n):
            return fib(n+1)-1
        sum=sum_fib(B)-sum_fib(A-1)
        #print(cache)
        return sum%MOD
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solv(self, A, B):
        mod = 10**9 + 7
        
        class Matrix2x2:
            Class to represent a 2x2 matrix seen like this :
                    a   b
                    c   d
            def __init__(self, a, b, c, d):
                self.a = a
                self.b = b
                self.c = c
                self.d = d
            def __mul__(self, matrix):
                a = ((self.a * matrix.a)%mod + (self.b* matrix.c)%mod)%mod
                b = ((self.a * matrix.b)%mod+ (self.b* matrix.d)%mod)%mod
                c = ((self.c * matrix.a)%mod+ (self.d* matrix.c)%mod)%mod
                d = ((self.c * matrix.b)%mod+ (self.d* matrix.d)%mod)%mod
                return Matrix2x2(a, b, c, d)
        
            def fastExp(self, exponent) :
                base = Matrix2x2(self.a, self.b, self.c, self.d)
                result = Matrix2x2(1, 0, 0, 1)
                while exponent > 0 :
                    if exponent %2== 1 :
                        result = result * base
                    base = base * base
                    exponent //= 2
                return result

        def fibonacci( n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return Matrix2x2(1, 1, 1, 0).fastExp(n-1).a
        
        ans= fibonacci( B+2)-fibonacci( A+1)
        return ans if ans>=0 else ans%mod
"""
