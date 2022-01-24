#https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #Sol1: T: O(M+N) S: O(1)
        n1 = m - 1
        n2 = n - 1
        for p in range (m+n-1,-1, -1): //Start from end of nums1 array
            if n2 < 0 :
                break
            if n1 >= 0 and nums1[n1] > nums2[n2] :
                nums1[p] = nums1[n1]
                n1 -= 1
            else:
                nums1[p] = nums2[n2]
                n2 -= 1
