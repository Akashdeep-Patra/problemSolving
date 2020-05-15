"""
Numbers of length N and value less than K
Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.
 NOTE: All numbers can only have digits from the given set. 
Examples:
    Input:
      0 1 5  
      1  
      2  
    Output:  
      2 (0 and 1 are possible)  

    Input:
      0 1 2 5  
      2  
      21  
    Output:
      5 (10, 11, 12, 15, 20 are possible)
Constraints:
    1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9

"""


from bisect import bisect_left
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def solve(self, a, length, number):
	    if(a==[]):
	        return 0
	    if(length==1):
	        return bisect_left(a,number,0,len(a))
	    number=list(map(int,list(str(number))))
	    if(length>len(number)):
	        return 0
	    elif(length<len(number)):
	        if(a[0]==0):
	            return len(a)**(length-1)*(len(a)-1)
	        return len(a)**length
	   # if(len(a)==1):
	   #     if(number[0]>a[0]):
	   #         return 1
	   #     return 0
	    n=len(number)
	    ans=0
	   # print(number)
	    for i in range(len(number)):
	        index=bisect_left(a,number[i],0,len(a))
	       # print("index",index)
	        if(index!=len(a)  and a[index]!=number[i]):
	            if(a[0]==0 and i==0):
	                index-=1
	            ans+=index*(len(a)**(n-1-i))
	            break
	        elif(index==len(a)):
	            if(a[0]==0 and i==0):
	                index-=1
	            ans+=index*(len(a)**(n-1-i))
	            break
	        else:
	            if(a[0]==0 and i==0):
	                index-=1
	            ans+=index*(len(a)**(n-1-i))
	    return ans
	            
	        
