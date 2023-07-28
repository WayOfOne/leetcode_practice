# https://leetcode.com/problems/two-sum/

# use dictionary to store a value and the index of each element in the list of int
# O(n) time and O(n) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], index]
            d[num]=index