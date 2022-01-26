#https://leetcode.com/problems/meeting-rooms/
#Sol1: T: O(nlogn) S: O(1)

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
