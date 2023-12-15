# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q=[]
        if not root:
            return root
        res=[]

        q.append(root)
        while q:
            size = len(q)
            m=-math.inf
            for i in range(size):
                temp = q.pop(0)
                m = max(m,temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

            res.append(m)

        return res

        