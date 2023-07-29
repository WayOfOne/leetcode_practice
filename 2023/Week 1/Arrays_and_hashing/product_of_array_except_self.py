# https://leetcode.com/problems/product-of-array-except-self/description/

# can't use division

# create 2 lists of intermediate products and just multiply them since you can't use division
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    size = len(nums)
    left = [1] * size
    right = [1] * size

    # list of products of all elements to the left of i
    # left[0] = 1 by default
    for i in range(1, size):
        left[i] = left[i - 1] * nums[i - 1]

    # list of products of all elements to the right of i
    for i in range(size - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # multiply the two lists
    return [left[i] * right[i] for i in range(size)]
