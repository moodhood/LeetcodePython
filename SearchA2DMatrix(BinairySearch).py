class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        Rows, Collumn = len(matrix), len(matrix[0])
        Top, Bottom = 0, Rows-1

        while Top <= Bottom:
            mid = (Top+Bottom)//2
            if target > matrix[mid][-1]:
                Top = mid + 1 
            elif target < matrix[mid][0]:
                Bottom = mid - 1
            else:
                break
        

        if not (Top <= Bottom):
            return False
        row = (Top+Bottom)//2
        l, r = 0, Collumn-1

        while l <= r:
            mid = (l+r)//2
            if target > matrix[row][mid]:
                l = mid + 1 
            elif target < matrix[row][mid]:
                r = mid - 1 
            else: 
                return True
        return False 
