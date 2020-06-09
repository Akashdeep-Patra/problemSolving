class Solution:
    # @param A : string
    # @return a strings
    def solve(self, a):
        mem = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        stack = []
        ans = []
        for c in a:
            if c == ")":
                while (stack[-1] != "("):
                    ans.append(stack.pop())
                stack.pop()
            elif (c == "("):
                stack.append(c)
            elif c in mem:
                while (len(stack) != 0 and stack[-1] != "("
                       and mem[c] <= mem[stack[-1]]):
                    ans.append(stack.pop())
                stack.append(c)
            else:
                ans.append(c)
        for c in stack[::-1]:
            ans.append(c)
        return "".join(ans)


"""
Infix to Postfix
Problem Description

Given string A denoting an infix expression. Convert the infix expression into postfix expression.

String A consists of ^, /, *, +, -, (, ) and lowercase english alphabets where lowercase english alphabets are operands and ^, /, *, +, - are operators.

Find and return the postfix expression of A.

NOTE:

^ has highest precedence.
/ and * have equal precedence but greater than + and -.
+ and - have equal precedence and lowest precedence among given operators.


Problem Constraints
1 <= length of the string <= 500000



Input Format
The only argument given is string A.



Output Format
Return a string denoting the postfix conversion of A.



Example Input
Input 1:

 A = "x^y/(a*z)+b"
Input 2:

 A = "a+b*(c^d-e)^(f+g*h)-i"


Example Output
Output 1:

 "xy^az*/b+"
Output 2:

 "abcd^e-fgh*+^*+i-"


Example Explanation
Explanation 1:

 Ouput dentotes the postfix expression of the given input.
"""
