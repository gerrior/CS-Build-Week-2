# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: [int], target: int) -> int:
        index = -1

        for num in nums:
            index += 1
            if num == target:
                return index

        return -1

a = Solution()
# 4
print(a.search([4,5,6,7,0,1,2], 0))
# -1
print(a.search([4,5,6,7,0,1,2], 3))

