"""
Count of divisors for multiple queries
Problem Description
Given an array of integers A, find and return the count of divisors of each element of the array. NOTE: Order of the resultant array should be same as the input array.     


Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 106


Input Format
The only argument given is the integer array A.


Output Format
Return the count of divisors of each element of the array in the form of an array.


Example Input
Input 1:
 A = [2, 3, 4, 5]
Input 2:
 A = [8, 9, 10]


Example Output
Output 1:
 [2, 2, 3, 2]
Output 1:
 [4, 3, 4]


Example Explanation
Explanation 1:
 The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
 So the count will be [2, 2, 3, 2].
Explanation 2:
 The number of divisors of 8 : [1, 2, 4, 8], 9 : [1, 3, 9], 10 : [1, 2, 5, 10]
 So the count will be [4, 3, 4].




"""








from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, a):
        n=max(a)
        spf=[x for x in range(n+1)]
        def seive(n):
            i=2
            while(i*i<=n):
                if spf[i]==i:
                    for p in range(i*i,n+1,i):
                        if(spf[p]==p):
                            spf[p]=i
                i+=1
        seive(n)
        old=0
        new=0
        anss=[]
        for x in a:
            ans=1
            old=spf[x]
            counter=0
            while(x>1):
                new=spf[x]
                if(old==new):
                    counter+=1
                else:
                    old=new
                    ans*=(counter+1)
                    counter=1
                x=x//new
            ans*=(counter+1)
            anss.append(ans)
            
        return anss