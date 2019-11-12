# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:return 0
        l,r=0,len(rotateArray)
        while l+1<r:
            mid=(l+r)//2
            if rotateArray[mid]>=rotateArray[l]:
                l=mid
            else:
                r=mid
                
        return rotateArray[r]
        
        