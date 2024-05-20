from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        Row = defaultdict(set)
        Column = defaultdict(set)
        Box = defaultdict(set)
        for row in range(9):
            for column in range(9):
                if (board[row][column] == "."):
                    continue
                if(board[row][column] in Row[row]):
                    return False
                if(board[row][column] in Column[column]):
                    return False
                if(board[row][column] in Box[(row//3,column//3)]):
                    return False
            
                Row[row].add(board[row][column])
                Column[column].add(board[row][column])
                Box[(row//3,column//3)].add(board[row][column])
        return True





