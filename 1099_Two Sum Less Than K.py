#https://leetcode.com/problems/two-sum-less-than-k/
#Sol1: T: O(n) S: O(n)

class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        low = 0
        high = len(nums) - 1
        result = -1
        while (low < high):
            sum = nums[low] + nums[high]
            if (sum < k):
                result = max(result, sum)
                low += 1
            else:
                high -= 1
        return result
            
