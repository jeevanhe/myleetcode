#https://leetcode.com/problems/3sum-closest/
#Sol1: T: O(n2) S: O(1)

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            low = i +1
            high = len(nums) - 1
            while (low < high):
                sum = nums[i] + nums[low] + nums[high]
                if abs(target - sum) < abs(diff): # latest diff better than previous one?
                    diff = target - sum
                if sum < target:
                    low += 1
                else:
                    high -= 1
                if diff == 0 : #sum and target are same
                    break
        return target - diff
