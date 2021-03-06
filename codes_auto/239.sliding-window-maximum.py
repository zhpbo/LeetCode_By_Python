#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] sliding-window-maximum
#
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        n = len(nums)
        if n <= k: return [max(nums)]
        res = []
        for i in range(n - k+1):
            res+=[max(nums[i:i+k])]
        return res
# @lc code=end