# https://leetcode.com/problems/contains-duplicate/
# Time complexity:
# Space complexity:
# Notes:
"""
Naive method: Two loops comparing i with i + 1 item and loop for match and return. 
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        #print(nums)
        #print(set(nums))
        #print(len(set(nums)))                        
    
        #Sol1: T: O(n2) S: O(1)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return 1
        return 0
        """

        #Sol2: T: O(nlogn) S: O(1)
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] :
                return 1
        return 0
        """
        
        #Sol3:
        """"
        for i in nums:
            if nums.count(i) > 1:
                return 1
        return 0
        """
        
        #Sol4 :
        return len(nums) > len(set(nums))
    
        


