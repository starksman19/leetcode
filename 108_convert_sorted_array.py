from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide_and_conquer(n):
            if len(n) == 0:
                return None

            m = len(n) // 2
            node = TreeNode(n[m])

            node.left = divide_and_conquer(n[:m])
            node.right = divide_and_conquer(n[m + 1 :])
            return node

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        if len(nums) <= 1:
            return root

        root.left = divide_and_conquer(nums[:mid])
        root.right = divide_and_conquer(nums[mid + 1 :])
        return root


nums = [-10, -3, 0, 5, 9]
print(Solution().sortedArrayToBST(nums))
