# https://leetcode.com/problems/contains-duplicate/

# basically use any dictionary/hashmap to keep hold elements of the input and look up if item already exists
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = dict.get(i, 0) + 1
        return False


# fancy python solution using set since set internally is basically a dictionary
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
