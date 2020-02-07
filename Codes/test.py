'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, tem = [], []
        nums.sort()
        len_nums = len(nums)
        check = [0 for _ in range(len_nums)]
        # 调用回溯函数
        self.backtrack(nums, tem, res, check)
        return res

    # 回溯函数
    def backtrack(self, nums, tem, res, check):
        if len(tem) == len(nums):
            res.append(tem[:])
        else:
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                tem.append(nums[i])
                # 去除第i个元素的部分
                self.backtrack(nums, tem, res,check)
                check[i] = 0
        if tem == []:  # 无法pop的情况
            return
        tem.pop()


if __name__ == '__main__':
    S = Solution()
    res = S.permuteUnique([1, 1, 3])
    print(res)
