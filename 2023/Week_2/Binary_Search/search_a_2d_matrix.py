class Solution:
    # searching in a 2D matrix sorted matrix
    # the first element of each row is greater than the last element of the previous row
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # O(log(mn)) time complexity, O(1) space complexity
        # m is the number of rows, n is the number of columns
        # the matrix is sorted, so we can treat it as a 1D array
        # we can use the same binary search algorithm as in 2023\Week 2\Binary_Search\search_in_rotated_sorted_array.py
      
        # the number of rows
        rows = len(matrix)
        # the number of columns
        columns = len(matrix[0])
        # the leftmost index
        left = 0
        # the rightmost index
        right = rows - 1
      