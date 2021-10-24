# reference
# https://blog.csdn.net/fuxuemingzhu/article/details/79363903

from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """

        return list(permutations(nums))

# a simple example
myNums = [2, 1, 4]
sol = Solution()
print(sol.permute(myNums))