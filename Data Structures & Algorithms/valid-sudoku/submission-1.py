class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows= [set() for _ in range(9)] # creates set(),set(),set()...until 9]
        columns=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        col=0
        row=0
        #handles duplicates in rows and columns also adds values in set
        for rowIndex in range(len(board)):#0 unti 8
            for columnIndex in range(len(board[rowIndex])):#0 unti 8
               if board[rowIndex][columnIndex] in rows[rowIndex] or board[rowIndex][columnIndex] in columns[columnIndex]:
                return False 
               if board[rowIndex][columnIndex]!=".":
                rows[rowIndex].add(board[rowIndex][columnIndex])
                columns[columnIndex].add(board[rowIndex][columnIndex])
                boxIndex = (rowIndex // 3) * 3 + (columnIndex // 3)
                if board[rowIndex][columnIndex] in box[boxIndex]:
                 return False
                box[boxIndex].add(board[rowIndex][columnIndex])
                
               
        
    
        
        return True
            


            
            

        