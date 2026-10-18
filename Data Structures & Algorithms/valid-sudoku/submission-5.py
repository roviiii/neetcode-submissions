class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows=[set() for _ in range(len(board)) ]
        columns=[set() for _ in range(len(board)) ]
        box=[set()for _ in range(len(board))]


        for rowIndex in range(len(board)):
          for columnIndex in range(len(board)):
            value=board[rowIndex][columnIndex]
            if value !=".":
                
                boxIndex=(rowIndex//3)*3+(columnIndex//3)
                
                if value in rows[rowIndex] or value in columns[columnIndex] or value in box[boxIndex]:
                    return False
            
                rows[rowIndex].add(value)
                columns[columnIndex].add(value)
                box[boxIndex].add(value)



        return True 

        