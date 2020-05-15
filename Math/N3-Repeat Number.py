"""
N/3 Repeat Number
You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space. If so, return the integer. If not, return -1. If there are multiple solutions, return any one. Example :
Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 

"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, a):
        max1=1.2
        max2=1.2
        count1=0
        count2=0
        for i in a:
            if(i!=max1 and i!=max2):
                if(count1==0):
                    max1=i
                    count1=1
                    continue
                elif(count2==0):
                    max2=i
                    count2=1
                    continue
                count1-=1
                count2-=1
            if(i==max1):
                count1+=1
            if(i==max2):
                count2+=1
        count1=0
        count2=0
        for i in a:
            if(i==max1):
                count1+=1
            if(i==max2):
                count2+=1
        if(count1>len(a)//3):
            return max1
        if(count2>len(a)//3):
            return max2
        return -1

        

                


	    

        



        

	        
