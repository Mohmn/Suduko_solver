class Suduko:

    def __init__(self,board):

        self.empty_spaces = 0
        self.size = board[0].length
        self.board = board
        self.numbers = [str(i) for i in range(1,10)]

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == '.':
                    self.empty_spaces +=1

    def valid_move(self,pos,num_to_check):

        row,col = pos[0],pos[1]

        # check rows 
        if num_to_check in self.board[row]:
            return False

        # check column
        if num_to_check in [self.board[i][col] for i in range(self.size)]:
            return False

        # check grid 
        
        # e.g  (0 to 2) // 3 == 0  (3,5)//3 == 1) and (1 * 3 == 3))   (6,8)//3 == 3 and (2*3 == 6) giving the starting grid positions
#       adding 3 to starting positions gives us ending grid positions

        box_row,box_col = row//3 *3,col//3 *3   

        for x in range(box_row,box_row + 3):
            for y in range(box_col,box_col+3):
                if self.board[x][y] == num_to_check:
                    return False
        return True


    def solve(self,row,col):
        # if the spaces are none then it means the board is filled
        if self.empty_spaces == 0:
            
            return True
#     search through all empty values and try out numbers(1-10) for each value
        while row < self.size:
            while col < self.size:
                
                if self.board[row][col] == '.':
                    
                    for num in self.numbers:
                        
                        if self.valid_move((row,col),num): # row,col,area
                            
                            self.board[row][col] = num
                            self.empty_spaces -= 1

                            if self.solve(row,col+1):
                                return True

                            self.board[row][col] = '.'
                            self.empty_spaces += 1
                            
                    # if none of the numbers work then return false
                    return False
                
                col += 1
            row += 1
            col = 0
