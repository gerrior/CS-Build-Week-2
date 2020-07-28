# https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        
        for digit in nums:
            if digit in dictionary:
                dictionary[digit] = True 
            else:
                dictionary[digit] = False 

        for key, value in dictionary.items():
            if value == True:
                return True
        
        return False