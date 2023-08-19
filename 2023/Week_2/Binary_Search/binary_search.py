
## write a method that does a binary search on a sorted array of integers to find a target integer
## return the index of the target integer if it exists in the array, otherwise return -1
## https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # iterative solution
        # divide and conquer: keep dividing the array in half until the target is found   
        left = 0
        right = len(nums) - 1
        while left <= right:
            # integer division to get the middle index
            mid = (right + left) // 2
            # if the target is equal to the middle element, ding ding ding
            if target == nums[mid]:
                return mid
            # if the target is less than the middle element, search the left half
            elif target < nums[mid]:
                right = mid - 1
            # if the target is greater than the middle element, search the right half
            else:
                left = mid + 1
        # if the target is not found, return -1 since the target does not exist in the array
        return -1

        # recursive way
        # return self.binary_search(nums, target, 0, len(nums) - 1)
        
    def binary_search(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.binary_search(nums, target, left, mid - 1)
        else:
            return self.binary_search(nums, target, mid + 1, right)
            