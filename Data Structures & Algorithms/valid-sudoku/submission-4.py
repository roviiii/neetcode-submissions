class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows= [set() for _ in range(9)] # creates set(),set(),set()...until 9]
        columns=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        #handles duplicates in rows and columns also adds values in set
        for rowIndex in range(len(board)):#0 unti 8
            for columnIndex in range(len(board[rowIndex])):#0 unti 8
                if board[rowIndex][columnIndex] != ".":
                    value = board[rowIndex][columnIndex]
                    boxIndex = (rowIndex // 3) * 3 + (columnIndex // 3)
                    if (
                        value in rows[rowIndex]
                        or value in columns[columnIndex]
                        or value in box[boxIndex]
                    ):
                        return False

                    rows[rowIndex].add(value)
                    columns[columnIndex].add(value)
                    box[boxIndex].add(value)
                
               
        
    
        
        return True
            


            
            

        