"""
Points inside Rectangle
Problem Description
You are given a rectangle with co-ordinates represented by arrays A and B, where the sides might not be parallel to the x-y axis. Given N points on x-y plane whose co-ordinates are represented by arrays C and D, count the number of points that lie strictly inside the rectangle. All the coordinates have integral values.    


Problem Constraints
1 <= N <= 102 -107 <= A[i], B[i], C[i], D[i] <= 107   


Input Format
First arguement is an interger array A of size 4 denoting the x co-ordinates of all the four corners of the rectangle. Second arguement is an interger array B of size 4 denoting the y co-ordinates of all the four corners of the rectangle. Third argument is an integer array C of size N denoting the x co-ordinates of all the N points. Fourth argument is an integer array D of size N denoting the y co-ordinates of all the N points.    


Output Format
Return an single integer denoting the count of points that lies strictly inside the rectangle.


Example Input
Input 1:
 A = [0, -2, 2, 4]
 B = [0, 2, 6, 4]
 C = [1, 2, 1, 5, -3]
 D = [3, 4, 2, 5, 1]
   


Example Output
Output 1:
 3
   


Example Explanation
Explanation 1:
 Thus, rectangle has the coordinates (0,0), (-2,2), (2,6) and (4,4).
 We see points (1, 3), (2, 4), (1, 2) lies strictly inside the rectangle whereas (5, 5), (-3, 1) lies outside the rectangle

"""

def getArea(a,b,c):
    return  abs((c[0]*(a[1]-b[1])+a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])))
def isInside(a,b,c,d,p):
    s=0
    t=getArea(a,b,p)
    if(t==0):
        return False
    s+=t
    t=getArea(b,c,p)
    if(t==0):
        return False
    s+=t
    t=getArea(c,d,p)
    if(t==0):
        return False
    s+=t
    t=getArea(d,a,p)
    if(t==0):
        return False
    s+=t
    return s==getArea(a,b,c)+getArea(c,d,a)


class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @param C : list of integers
	# @param D : list of integers
	# @return an integer
	def solve(self, a, b, c, d):
	    ans=0
	    A=[a[0],b[0]]
	    B=[a[1],b[1]]
	    C=[a[2],b[2]]
	    D=[a[3],b[3]]
	    for i in range(len(c)):
	        p=[c[i],d[i]]
	        if(isInside(A,B,C,D,p)):
	            ans+=1
	    return ans

	            
	        
