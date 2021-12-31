#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Sol1: T: O(n2) S: O(1)
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (target == nums[i] + nums[j]):
                    return [i,j]
        return[]
        """
        #Sol2: T: O(n) S: O(n) Note: Sol2 can be split into 2 pass
        dict = {}
        for i, first in enumerate(nums):
            second = target - first
            if second in dict:
                return[dict[second], i]
            else:
                dict[first] = i
