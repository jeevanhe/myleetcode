#https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Sol1: T: O(n2) S: O(1) Brute Force
        """
        maxi = -sys.maxint - 1
        for i in range(len(nums)):
            temp_max = 0
            for j in range(i,len(nums)):
                temp_max = temp_max + nums[j]
                maxi = max(maxi, temp_max)
        return maxi
        """     
        #Sol2: T: O(n) S: O(1) Kadane Algorithm
        global_max = -sys.maxint-1
        local_max = 0
        for item in nums:
            local_max = max(item, local_max + item)
            global_max = max(local_max, global_max)
        return global_max
            
