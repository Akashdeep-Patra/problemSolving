def mul(a,b):
    return a*b
def add(a,b):
    return a+b
def div(a,b):
    return a//b
def dif(a,b):
    return a-b
class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, a):
	    mem={"+":add,"-":dif,"*":mul,"/":div}
	    stack=[]
	    for c in a:
	        if c in mem:
	            x=stack.pop()
	            y=stack.pop()
	            stack.append(mem[c](y,x))
	        else:
	            stack.append(int(c))
	    return stack[-1]

"""
Evaluate Expression
Problem Description

An arithmetic expression is given by a charater array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or operator.



Problem Constraints
1 <= N <= 105



Input Format
The only argument given is character array A.



Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.



Example Input
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Input 2:
    A = ["4", "13", "5", "/", "+"]


Example Output
Output 1:
    9
Output 2:
    6


Example Explanation
Explaination 1:
    starting from backside:
    * : () * ()
    3 : () * (3)
    + : (() + ()) * (3)
    1 : (() + (1)) * (3)
    2 : ((2) + (1)) * (3)
    ((2) + (1)) * (3) = 9
Explaination 2:
    + : () + ()
    / : () + (() / ())
    5 : () + (() / (5))
    1 : () + ((13) / (5))
    4 : (4) + ((13) / (5))
    (4) + ((13) / (5)) = 6
"""