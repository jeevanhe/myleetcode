#https://leetcode.com/problems/3sum-smaller/
#Sol1: T: O(n2) S: O(1)

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        triplets = 0
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if nums[i] + nums[low] + nums[high] < target:
                    triplets += high - low #array is sorted so
                    low += 1
                else:
                    high -= 1
        return triplets
