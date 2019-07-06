class Piece_King:
    def __init__(self, num, x, y, player):
        self.piece_type = 'KING'
        self.num = num
        self.x = x
        self.y = y
        self.player = player

    def move_set(self, board):
        moveset = []
        if self.y > 1:
            if not board.is_opponent_piece_at_location( self.x,
                                                     self.y - 1) and not self.player:  # move forward player not com
                moveset.append((self.x, self.y - 1))
            if self.x > 1 and not board.is_opponent_piece_at_location( self.x - 1,
                                                                    self.y - 1) and not self.player:  # move forward right not com
                moveset.append((self.x - 1, self.y - 1))
            if self.x < 9 and not board.is_opponent_piece_at_location( self.x + 1,self.y - 1) and not self.player:  # move forward left not com
                moveset.append((self.x + 1, self.y - 1))

            if not board.is_player_piece_at_location(self.getId(),self.x,self.y - 1) and self.player:  # move forward opponent com
                if not board.will_king_be_in_check(self.x, self.y - 1):
                    moveset.append((self.x, self.y - 1))
            if self.x > 1 and not board.is_player_piece_at_location(self.getId(),self.x - 1,self.y - 1) and self.player :  # move forward right com
                if not board.will_king_be_in_check(self.x - 1, self.y - 1):
                    moveset.append((self.x - 1, self.y - 1))
            if self.x < 9 and not board.is_player_piece_at_location(self.getId(),self.x + 1,self.y - 1) and self.player:  # move forward left com
                if not board.will_king_be_in_check(self.x + 1, self.y - 1):
                    moveset.append((self.x + 1, self.y - 1))

        if self.y < 9:
            if not board.is_opponent_piece_at_location( self.x,self.y + 1) and not self.player:  # move down not com
                moveset.append((self.x, self.y + 1))
            if self.x > 1 and not board.is_opponent_piece_at_location( self.x - 1,self.y + 1) and not self.player:  # move back right not com
                moveset.append((self.x - 1, self.y - 1))
            if self.x < 9 and not board.is_opponent_piece_at_location( self.x + 1,self.y + 1) and not self.player:  # move back left not com
                moveset.append((self.x + 1, self.y - 1))

            if not board.is_player_piece_at_location(self.getId(),self.x,self.y + 1) and self.player :  # move down com
                if not board.will_king_be_in_check(self.x, self.y + 1):
                    moveset.append((self.x, self.y + 1))
            if self.x > 1 and not board.is_player_piece_at_location(self.getId(),self.x - 1,self.y + 1) and self.player :  # move back right com
                if not board.will_king_be_in_check(self.x - 1, self.y + 1):
                    moveset.append((self.x - 1, self.y + 1))
            if self.x < 9 and not board.is_player_piece_at_location(self.getId(),self.x + 1,self.y + 1) and self.player :  # move back left com
                if not board.will_king_be_in_check(self.x + 1, self.y + 1):
                 moveset.append((self.x + 1, self.y + 1))

        if self.x > 1 and not board.is_opponent_piece_at_location( self.x - 1,self.y) and not self.player:  # move right not com
            moveset.append((self.x - 1, self.y))
        if self.x < 9 and not board.is_opponent_piece_at_location( self.x + 1,self.y) and not self.player:  # move left not com
            moveset.append((self.x + 1, self.y))

        if self.x > 1 and not board.is_player_piece_at_location(self.getId(),self.x - 1,self.y) and self.player :  # move right com
            if not board.will_king_be_in_check(self.x - 1, self.y ):
                moveset.append((self.x - 1, self.y))
        if self.x < 9 and not board.is_player_piece_at_location(self.getId(),self.x + 1,self.y) and self.player :  # move left com
            if not board.will_king_be_in_check(self.x + 1, self.y):
                moveset.append((self.x + 1, self.y))

        return moveset

    def getId(self):
        return self.num

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y


class Piece_Gold:
    def __init__(self, pid, x, y, player):
        self.piece_type = 'GOLD'
        self.num = pid
        self.x = x
        self.y = y
        self.player = player
        self.isTaken = False
        if self.x > 9:
            self.isTaken = True

    def move_set(self, board):
        moveset = []
        if self.y > 1:
            if not board.is_opponent_piece_at_location( self.x,self.y - 1) and not self.player:  # not com down
                moveset.append((self.x, self.y - 1))



            if not board.is_player_piece_at_location(self.getId(), self.x, self.y - 1) and self.player:  # com forward
                moveset.append((self.x, self.y - 1))
            if self.x > 1 and not board.is_player_piece_at_location(self.getId(), self.x - 1,self.y - 1) and self.player:  # com leftsown
                moveset.append((self.x - 1, self.y - 1))
            if self.x < 9 and not board.is_player_piece_at_location(self.getId(), self.x + 1,self.y - 1) and self.player:  # com right down
                moveset.append((self.x + 1, self.y - 1))

        if self.y < 9:
            if  not board.is_player_piece_at_location(self.getId(), self.x, self.y + 1) and self.player: #com down
                moveset.append((self.x, self.y + 1))
            if not board.is_opponent_piece_at_location( self.x, self.y + 1) and not self.player:  # not com up
                moveset.append((self.x, self.y + 1))

            if self.x > 1 and not board.is_opponent_piece_at_location( self.x - 1,self.y + 1) and not self.player:  # not com left up
                moveset.append((self.x - 1, self.y + 1))
            if self.x < 9 and not board.is_opponent_piece_at_location( self.x + 1,self.y + 1) and not self.player:  # not com right up
                moveset.append((self.x + 1, self.y + 1))

        if self.x > 1 and not board.is_player_piece_at_location(self.getId(), self.x - 1, self.y) and  self.player: # com left
            moveset.append((self.x - 1, self.y))
        if self.x < 9 and not board.is_player_piece_at_location(self.getId(), self.x + 1, self.y) and  self.player: # com right
            moveset.append((self.x + 1, self.y))

        if self.x > 1 and not board.is_opponent_piece_at_location( self.x - 1, self.y)and not self.player: #not com right
            moveset.append((self.x - 1, self.y))
        if self.x < 9 and not board.is_opponent_piece_at_location( self.x + 1, self.y)and not self.player: #not com left
            moveset.append((self.x + 1, self.y))


        if self.isTaken:
            for row in range(1, 9):
                for col in range(1, 9):
                    if not board.is_player_piece_at_location(self.getId(), row,col) and not board.is_opponent_piece_at_location(row, col):
                        moveset.append((row, col))
        return moveset

    def getId(self):
        return self.num

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y


class Piece_Silver:
    def __init__(self, pid, x, y, player):
        self.piece_type = 'SILVER'
        self.num = pid
        self.x = x
        self.y = y
        self.player = player
        self.promoted = False
        self.isTaken = False
        if self.x > 9:
            self.isTaken = True

        def setx(self, x):
            self.x = x

        def sety(self, y):
            self.y = y

    def move_set(self, board):
        moveset = []
        if self.y < 9 and not self.player:
            if not board.is_opponent_piece_at_location( self.x, self.y + 1) : #not com forward
                moveset.append((self.x, self.y + 1))
            if self.x > 1 and not board.is_opponent_piece_at_location( self.x - 1, self.y + 1): #not com forward left
                moveset.append((self.x - 1, self.y + 1))
            if self.x < 9 and not board.is_opponent_piece_at_location( self.x + 1, self.y + 1): #not com forward right
                moveset.append((self.x + 1, self.y + 1))
        if self.y > 1 and not self.player:
            if self.x > 1 and not board.is_opponent_piece_at_location( self.x - 1, self.y - 1): #not com back left
                moveset.append((self.x - 1, self.y - 1))
            if self.x < 9 and not board.is_opponent_piece_at_location( self.x + 1, self.y - 1): #not com back right
                moveset.append((self.x + 1, self.y - 1))

        if self.y > 1 and  self.player:
            if not board.is_player_piece_at_location(self.getId(), self.x, self.y - 1): #com forward
                moveset.append((self.x, self.y - 1))
            if self.x > 1 and not board.is_player_piece_at_location(self.getId(), self.x - 1, self.y - 1): #com forward left
                moveset.append((self.x - 1, self.y - 1))
            if self.x < 9 and not board.is_player_piece_at_location(self.getId(), self.x + 1, self.y - 1): #com forward right
                moveset.append((self.x + 1, self.y - 1))
        if self.y < 9 and  self.player:
            if self.x > 1 and not board.is_player_piece_at_location(self.getId(), self.x - 1, self.y + 1): #com  backleft
                moveset.append((self.x - 1, self.y - 1))
            if self.x < 9 and not board.is_player_piece_at_location(self.getId(), self.x + 1, self.y - 1): #com back right
                moveset.append((self.x + 1, self.y - 1))
        if self.isTaken:
            for row in range(1, 9):
                for col in range(1, 9):
                    if not board.is_player_piece_at_location(self.getId(), row,
                                                             col) and not board.is_opponent_piece_at_location(row, col):
                        moveset.append((row, col))
        return moveset

    def getId(self):
        return self.num

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y


class Piece_Horse:
    def __init__(self, pid, x, y, player):
        self.piece_type = 'HORSE'
        self.num = pid
        self.x = x
        self.y = y
        self.player = player
        self.promoted = False
        self.isTaken = False
        if self.x > 9:
            self.isTaken = True

    def move_set(self, board):
        moveset = []
        if self.y < 8:
            if self.x > 1 and not board.is_opponent_piece_at_location( self.x - 1,
                                                                    self.y + 2) and not self.player:
                moveset.append((self.x - 1, self.y + 2))
            if self.x < 9  and not board.is_opponent_piece_at_location( self.x + 1,
                                                                    self.y + 2) and not self.player:
                moveset.append((self.x + 1, self.y + 2))
        if self.y > 2:       
            if self.x > 1 and not board.is_player_piece_at_location(self.getId(),self.x - 1,
                                                                      self.y - 2) and self.player:
                moveset.append((self.x - 1, self.y - 2))
            if self.x < 9 and not board.is_player_piece_at_location(self.getId(),self.x + 1,
                                                                      self.y - 2) and self.player:
                moveset.append((self.x + 1, self.y - 2))
        if self.isTaken:
            for row in range(1, 9):
                for col in range(1, 7):
                    if not board.is_player_piece_at_location(self.getId(), row,
                                                             col) and not board.is_opponent_piece_at_location(row, col):
                        moveset.append((row, col))
        return moveset

    def getId(self):
        return self.num

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y


class Piece_Castle:
    def __init__(self, pid, x, y, player):
        self.piece_type = 'CASTLE'
        self.num = pid
        self.x = x
        self.y = y
        self.player = player
        self.promoted = False
        self.isTaken = False
        if self.x > 9:
            self.isTaken = True

    def move_set(self, board):
        moveset = []
        if not self.player:
            init_y = self.y - 1
        else:
            init_y = self.y + 1
        if self.player:
            while init_y > 1:

                if board.is_player_piece_at_location(self.getId(), self.x, init_y):
                    break
                moveset.append((self.x, init_y))
                init_y -= 1
                if board.is_opponent_piece_at_location(self.x, init_y):
                    break
        else:
            while init_y < 9:
                if board.is_opponent_piece_at_location(self.x, init_y):
                    break
                moveset.append((self.x, init_y))
                init_y += 1
                if board.is_player_piece_at_location(self.getId(), self.x, init_y):
                    break

        if self.isTaken:
            for row in range(1, 9):
                for col in range(1, 8):
                    if not board.is_player_piece_at_location(self.getId(), row,
                                                             col) and not board.is_opponent_piece_at_location(row, col):
                        moveset.append((row, col))
        return moveset

    def getId(self):
        return self.num

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y


class Piece_Bishop:
    def __init__(self, pid, x, y, player):
        self.piece_type = 'BISHOP'
        self.num = pid
        self.x = x
        self.y = y
        self.player = player
        self.promoted = False
        self.isTaken = False
        if self.x > 9:
            self.isTaken = True

    def move_set(self, board):
        moveset = []
        init_y = self.y - 1
        init_x = self.x - 1
        while init_y > 1 and init_x > 1:
            if self.player:
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
            else:
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
            init_y -= 1
            init_x -= 1

        init_y = self.y - 1
        init_x = self.x + 1
        while init_y > 1 and init_x < 9:
            if self.player:
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
            else:
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
            init_y -= 1
            init_x += 1

        init_y = self.y + 1
        init_x = self.x - 1
        while init_y < 9 and init_x > 1:
            if self.player:
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
            else:
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
            init_y += 1
            init_x -= 1

        init_y = self.y + 1
        init_x = self.x + 1
        while init_y < 9 and init_x < 9:
            if self.player:
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
            else:
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
            init_y += 1
            init_x += 1
        if self.isTaken:
            for row in range(1, 9):
                for col in range(1, 9):
                    if not board.is_player_piece_at_location(self.getId(), row,
                                                             col) and not board.is_opponent_piece_at_location(row, col):
                        moveset.append((row, col))
        return moveset

    def getId(self):
        return self.num

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y


class Piece_Rook:
    def __init__(self, pid, x, y, player):
        self.piece_type = 'ROOK'
        self.num = pid
        self.x = x
        self.y = y
        self.player = player
        self.promoted = False
        self.isTaken = False
        if self.x > 9:
            self.isTaken = True

    def move_set(self, board):
        moveset = []
        init_y = self.y - 1
        init_x = self.x
        while init_y > 1:
            if  self.player:
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
            else:
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
            init_y -= 1

        init_y = self.y
        init_x = self.x + 1
        while init_x < 9:
            if  self.player:
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
            else:
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break

            init_x += 1

        init_y = self.y + 1
        init_x = self.x
        while init_y < 9:
            if  self.player:
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
            else:
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
            init_y += 1

        init_y = self.y
        init_x = self.x - 1
        while init_x > 1:
            if self.player:
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
            else:
                if board.is_opponent_piece_at_location(init_x, init_y):
                    break
                moveset.append((init_x, init_y))
                if board.is_player_piece_at_location(self.getId(), init_x, init_y):
                    break

            init_x -= 1
        if self.isTaken:
            for row in range(1, 9):
                for col in range(1, 8):
                    if not board.is_player_piece_at_location(self.getId(), row,
                                                             col) and not board.is_opponent_piece_at_location(row, col):
                        moveset.append((row, col))
        return moveset

    def getId(self):
        return self.num

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y


class Piece_Pawn:
    def __init__(self, num, x, y, player):
        self.piece_type = 'PAWN'
        self.num = num
        self.x = x
        self.y = y
        self.player = player
        self.promoted = False
        self.isTaken = False
        if self.x > 9:
            self.isTaken = True

    def move_set(self, board):
        moveset = []
        if self.player:
            if self.y > 1 and not board.is_player_piece_at_location(self.getId(), self.x,self.y - 1):
                moveset.append((self.x, self.y - 1))
        else:
            if self.y < 9 and not board.is_opponent_piece_at_location(self.x, self.y + 1):
                moveset.append((self.x, self.y + 1))

        if self.isTaken:
            for row in range(1, 9):
                for col in range(1, 8):
                    if not board.is_player_piece_at_location(self.getId(), row,
                                                             col) and not board.is_opponent_piece_at_location(row,
                                                                                                              col) and not self.player:
                        moveset.append((row, col))
        return moveset

    def getId(self):
        return self.num

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y


def PieceFactory(num, x, y, player):
    if num == 1 or num == 21:
        return Piece_King(num, x, y, player)

    if num == 2 or num == 3 or num == 22 or num == 23:
        return Piece_Gold(num, x, y, player)

    if num == 4 or num == 5 or num == 24 or num == 25:
        return Piece_Silver(num, x, y, player)

    if num == 6 or num == 7 or num == 26 or num == 27:
        return Piece_Horse(num, x, y, player)

    if num == 8 or num == 9 or num == 28 or num == 29:
        return Piece_Castle(num, x, y, player)

    if num == 10 or num == 30:
        return Piece_Bishop(num, x, y, player)

    if num == 11 or num == 31:
        return Piece_Rook(num, x, y, player)

    if (12 <= num <= 20) or (32 <= num <= 40):
        return Piece_Pawn(num, x, y, player)
