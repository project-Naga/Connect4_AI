import numpy as np

class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)

    def is_valid(self,board,col):
        if board[0,col]==0:
            return True
        else:
            return False
    
    def is_terminal_node(self,board):
        flag = True
        for col in range(7):
            if board[0,col] == 0:
                flag = False
        return flag
    
    def next_row(self,board,col):
        new_row = -1
        for row in range(6):
            if board[row,col] ==0 :
                new_row = row
        return new_row
    
    def alpha_beta_pruning(self,board,depth,alpha,beta,flag):
        if depth == 0 or self.is_terminal_node(board) == True:
            val = self.evaluation_function(board)
            if flag:
                return (None,-val)
            else:
                return (None,val)
        if flag :
            value = float("-inf")
            column = -1
            for col in range(7):
                if not self.is_valid(board,col):
                    continue
                new_row = self.next_row(board,col)
                board[new_row,col]=self.player_number

                score = self.alpha_beta_pruning(board,depth-1,alpha,beta,False)[1]
                board[new_row,col]=0
                if score > value:
                    value = score
                    column = col
                alpha = max(alpha,value)
                if alpha >= beta:
                    break
            return column,value
        else:
            value = float("inf")
            column = -1
            for col in range(7):
                if not self.is_valid(board,col):
                    continue
                new_row = self.next_row(board,col)
                board[new_row,col]=3-self.player_number
                score = self.alpha_beta_pruning(board,depth-1,alpha,beta,True)[1]
                board[new_row,col]=0
                if score < value:
                    value = score
                    column = col
                beta = min(beta,value)
                if alpha >= beta:
                    break
            return column,value
    
    
    def get_alpha_beta_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the alpha-beta pruning algorithm

        This will play against either itself or a human player

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        return self.alpha_beta_pruning(board,5,float("-inf"),float("inf"),True)[0]
        raise NotImplementedError('Whoops I don\'t know what to do')
    
    def expectimax(self,board,depth,flag):
        if depth == 0 or self.is_terminal_node(board) == True:
            val = self.evaluation_function(board)
            if flag:
                return (None,-val)
            else:
                return (None,val)
        column = -1
        if flag:
            value = float("-inf")
            for col in range(7):
                if not self.is_valid(board,col):
                    continue
                new_row = self.next_row(board,col)
                board[new_row,col] = self.player_number
                score = self.expectimax(board,depth-1,False)[1]
                board[new_row,col] = 0
                if score > value:
                    value = score
                    column = col
        else:
            value = 0
            for col in range(7):
                if not self.is_valid(board,col):
                    continue
                new_row = self.next_row(board,col)
                board[new_row][col] = 3-self.player_number
                score = self.expectimax(board,depth-1,True)[1]
                board[new_row][col] = 0
                value += score
            value = value //7
        return column,value
                
                

    def get_expectimax_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the expectimax algorithm.

        This will play against the random player, who chooses any valid move
        with equal probability

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        return self.expectimax(board,5,True)[0]
        raise NotImplementedError('Whoops I don\'t know what to do')
    
    def eval(self,window):
        score = 0
        length = len(window)
        for col in range(length):
            if col < length-1:
                if window[col] == window[col+1] == self.player_number:
                    if col!=0 :
                        if window[col-1] == 0:
                            score +=30
                            if col>=2 and window[col-2] == self.player_number:
                                score += 100
                    if col!=length-2 :
                        if window[col+2] == 0:
                            score +=30
                            if col<length-3 and window[col+3] == self.player_number:
                                score += 100
                if window[col] == window[col+1] == 3 - self.player_number:
                    if col!=0 :
                        if window[col-1] == 0:
                            score +=30
                            if col>=2 and window[col-2] == 3-self.player_number:
                                score += 100
                    if col!=length-2 :
                        if window[col+2] == 0:
                            score +=30
                            if col<length-3 and window[col+3] == 3-self.player_number:
                                score += 100
            if col < length-2:
                if window[col] == window[col+1] == window[col+2] == self.player_number:
                    if col!=0 :
                        if window[col-1] == 0:
                            score +=100
                        if window[col-1] == self.player_number:
                            score += 100000
                    if col!=length-3 :
                        if window[col+3] == 0:
                            score +=100
                        if window[col+3] == self.player_number:
                            score += 100000

                if window[col] == window[col+1] == window[col+2] == 3 - self.player_number:
                    if col!=0 :
                        if window[col-1] == 0:
                            score -=100
                        if window[col-1] == 3-self.player_number:
                            score -= 100000
                    if col!=length-3 :
                        if window[col+3] == 0:
                            score -=100
                        if window[col+3] == 3-self.player_number:
                            score -= 100000
        return score

    def evaluation_function(self, board):
        """
        Given the current stat of the board, return the scalar value that 
        represents the evaluation function for the current player
       
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The utility value for the current board
        """
        score = 0
        center_array = [int(i) for i in list(board[:, 3])]
        center_count = center_array.count(self.player_number)
        score += center_count * 20

        # Score Horizontal
        for r in range(6):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(4):
                window = row_array[c:c + 4]
                score += self.eval(window)

        # Score Vertical
        for c in range(7):
            col_array = [int(i) for i in list(board[:, c])]
        for r in range(3):
            window = col_array[r:r + 4]
            score += self.eval(window)

        # Score Diagonals
        for r in range(3):
            for c in range(4):
                window = [board[r + i][c + i] for i in range(4)]
                score += self.eval(window)

        for r in range(3):
            for c in range(4):
                window = [board[r + 3 - i][c + i] for i in range(4)]
                score += self.eval(window)
        return score                


class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state select a random column from the available
        valid moves.

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for col in range(board.shape[1]):
            if 0 in board[:,col]:
                valid_cols.append(col)

        return np.random.choice(valid_cols)


class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state returns the human input for next move

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """

        valid_cols = []
        for i, col in enumerate(board.T):
            if 0 in col:
                valid_cols.append(i)

        move = int(input('Enter your move: '))

        while move not in valid_cols:
            print('Column full, choose from:{}'.format(valid_cols))
            move = int(input('Enter your move: '))

        return move

