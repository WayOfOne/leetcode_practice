# https://leetcode.com/problems/product-of-array-except-self/description/

# can't use division

# create 2 lists of intermediate products and just multiply them since you can't use division
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    size = len(nums)
    left = [1] * size
    right = [1] * size

    for i in range(1, size):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(size - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    return [left[i] * right[i] for i in range(size)]
