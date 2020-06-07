from collections import defaultdict

def compute(a):
    mem=defaultdict(int)
    flag=1
    i=0
    sign_stack=[1]
    while(i<len(a)):
        if(a[i]=="("):
            if(i==0 or a[i-1]!="-"):
                sign_stack.append(1)
            else:
                sign_stack.append(-1)
                flag*=-1
        elif(a[i]==")"):
            flag=flag//sign_stack.pop()
        elif(a[i]!="+" and a[i]!="-"):
            if(a[i-1]=="-"):
                mem[a[i]]=flag*(-1)
            else:
                mem[a[i]]=flag
        i+=1
    return mem

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, a, b):
        a=compute(a)
        b=compute(b)
        # print(a)
        # print(b)
        if len(a.keys())!=len(b.keys()):
            return 0
        for key in a.keys():
            if(key not in b):
                return 0
            if(a[key]!=b[key]):
                return 0
        return 1


"""
Problem Description

Given two strings A and B. Each string represents an expression consisting of lowercase english alphabets, '+', '-', '(' and ')'.

The task is to compare them and check if they are similar. If they are similar return 1 else return 0.

NOTE: It may be assumed that there are at most 26 operands from ‘a’ to ‘z’ and every operand appears only once.



Problem Constraints
1 <= length of the each String <= 100



Input Format
The arguments given are string A and String B.



Output Format
Return 1 if they represent the same expression else return 0.



Example Input
Input 1:

 A = "-(a+b+c)"
 B = "-a-b-c"
Input 2:

 A = "a-b-(c-d)"
 B = "a-b-c-d"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The expression "-(a+b+c)" can be written as "-a-b-c" which is equal as B. 
Explanation 2:

 Both the expression are different.
"""