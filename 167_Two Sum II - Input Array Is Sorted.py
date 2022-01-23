#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Sol1: T: O(n) S: O(1) 
        low = 0
        high = len(numbers) - 1
        while low < high :
            if numbers[low] + numbers[high] == target :
                return [low + 1, high +1] #1-indexed array
            if numbers[low] + numbers[high] > target :
                high -= 1
            else :
                low +=1
