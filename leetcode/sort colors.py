class Solution:
    def sortColors(self, a: List[int]) -> None:
        z,o,t,i=0,0,0,0
        while(i<len(a)):
            while(t<len(a) and a[t]!=2 ):
                t+=1
            while(o<len(a) and a[o]!=1 ):
                o+=1
            while(z<len(a) and a[z]!=0 ):
                z+=1
            if(z<len(a)):
                a[i],a[z]=a[z],a[i]
                i+=1
                z+=1
            elif(o<len(a)):
                a[i],a[o]=a[o],a[i]
                i+=1
                o+=1
            else:
                a[i],a[t]=a[t],a[i]
                i+=1
                t+=1
        return a
            
        """
        Do not return anything, modify nums in-place instead.
        """
        



"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""