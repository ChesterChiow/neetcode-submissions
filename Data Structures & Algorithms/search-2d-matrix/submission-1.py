class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        leftRow, rightRow = 0, m - 1

        # Find which row first
        while leftRow <= rightRow:
            midRow = leftRow + ((rightRow - leftRow) // 2)
            if matrix[midRow][n-1] < target: # if last number in row less than target
                leftRow = midRow + 1
            elif matrix[midRow][0] > target: # if first number in row more than target
                rightRow = midRow - 1
            else:
                break
        
        if not (leftRow <= rightRow):
            return False
        
        # Find target in that row
        midRow = leftRow + ((rightRow - leftRow) // 2)
        l, r = 0, n - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[midRow][mid] > target:
                r = mid - 1
            elif matrix[midRow][mid] < target:
                l = mid + 1 
            else:
                return True
        return False
