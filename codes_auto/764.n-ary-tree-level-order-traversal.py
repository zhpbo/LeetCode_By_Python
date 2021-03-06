#
# @lc app=leetcode.cn id=764 lang=python3
#
# [764] n-ary-tree-level-order-traversal
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        d = root and [root]
        while d:
            yield [r.val for r in d]
            d = [t for r in d for t in r.children]
   
# @lc code=end