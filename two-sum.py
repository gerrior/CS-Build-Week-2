# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        index = -1
        
        # First throw the entire array into a dictory with the index value
        for num in nums:
            index += 1
            dict[num] = index

        index = -1
        # Go through each element again
        for num in nums:
            index += 1
            # Find what the other value needs to be
            candidate = target - num
            
            # Look up that value
            if candidate in dict:
                # Can't be the same value
                if dict[candidate] == index:
                    continue
                # Return the two indexes whose sum equals the target
                return [index, dict[candidate]]
                