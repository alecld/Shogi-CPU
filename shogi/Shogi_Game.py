import Shogi_Pieces as piece


class board:

    def __init__(self, piecesOne, xOne, yOne, piecesTwo, xTwo, yTwo, promotelist):
        self.playerOnePieces, self.playerTwoPieces, self.promotelist = build_board(piecesOne, xOne, yOne, piecesTwo,
                                                                                   xTwo, yTwo, promotelist)

    def get_board_as_arrays(self):
        player_piece_nums = []
        player_piece_x = []
        player_piece_y = []
        opp_piece_nums = []
        opp_piece_x = []
        opp_piece_y = []
        for piece in self.playerOnePieces:
            player_piece_nums.append(piece.num)
            player_piece_x.append(piece.x)
            player_piece_y.append(piece.y)
        for piece in self.playerTwoPieces:
            opp_piece_nums.append(piece.num)
            opp_piece_x.append(piece.x)
            opp_piece_y.append(piece.y)
        return player_piece_nums, player_piece_x, player_piece_y, opp_piece_nums, opp_piece_x, opp_piece_y, self.promotelist

    def move_piece_on_board(self, x_initial, y_initial, x_new, y_new):
        isMoved = False
        for player_piece in self.playerTwoPieces:
            if (player_piece.x == x_initial and player_piece.y == y_initial) and not \
                    self.is_player_piece_at_location(player_piece.num, x_new, y_new) and not \
                    (x_initial == x_new and y_initial == y_new):
                player_piece.setx(x_new)
                player_piece.sety(y_new)
                if(self.is_king_in_check()):
                    player_piece.setx(x_initial)
                    player_piece.sety(y_initial)
                else:
                    isMoved = True
                if self.is_opponent_piece_at_location(x_new, y_new):
                    taken_piece = self.get_opponent_piece_at_location(x_new, y_new)
                    self.move_to_taken_board(self.get_opponent_piece_at_location(x_new, y_new))
                    self.playerOnePieces.remove(taken_piece)
                    self.playerTwoPieces.append(taken_piece)
        return isMoved

    def is_player_piece_at_location(self, pid, x, y):
        for player_piece in self.playerTwoPieces:
            if player_piece.x == x and player_piece.y == y and player_piece.num != pid:
                return True

        return False

    def is_opponent_piece_at_location(self, x, y):
        for opp_piece in self.playerOnePieces:
            if opp_piece.x == x and opp_piece.y == y:
                return True

        return False

    def get_opponent_piece_at_location(self, x, y):
        for opp_piece in self.playerOnePieces:
            if opp_piece.x == x and opp_piece.y == y:
                return opp_piece

    def get_player_piece_at_location(self, x, y):
        for player_piece in self.playerTwoPieces:
            if player_piece.x == x and player_piece.y == y:
                return player_piece

    def move_to_taken_board(self, pie):
        if pie.piece_type == 'PAWN':
            pie.x = 13
            pie.y = 9
        if pie.piece_type == 'CASTLE':
            pie.x = 14
            pie.y = 9
        if pie.piece_type == 'HORSE':
            pie.x = 13
            pie.y = 9
        if pie.piece_type == 'SILVER':
            pie.x = 12
            pie.y = 9
        if pie.piece_type == 'GOLD':
            pie.x = 11
            pie.y = 9
        if pie.piece_type == 'BISHOP':
            pie.x = 13
            pie.y = 8
        if pie.piece_type == 'ROOK':
            pie.x = 12
            pie.y = 8
        if pie.piece_type == 'KING':
            pie.x = 14
            pie.y = 8

    # def is_piece_in_path(self, x_intial, y_initial, x_new, y_new):
    #     # get slope
    #     if x_new - x_intial != 0:
    #         slope = (y_new - y_initial) / (x_new - x_intial)
    #     else:
    #         slope = 0
    #          # determine direction and check path
    #     if slope == 1:
    #         if y_new > y_initial:
    #             # going right up
    #         else:
    #             # going down left
    #
    #     elif slope == -1:
    #         if y_new > y_initial:
    #             # going up left
    #         else:
    #             # going down right
    #     elif slope == 0:
    #         if y_initial > y_new and x_intial == x_new:
    #             # going sown
    #         elif y_initial < y_new and x_intial == x_new:
    #             # going up
    #         elif x_intial > x_new and y_new == y_initial:
    #             # going left
    #         else:
    #             # going right

    def is_king_in_check(self):

        x, y = self.get_player_piece_location_on_board(21)

        # look at every opponent piece moveset and see if any are the kings spot
        for pieces in self.playerOnePieces:
            for move in pieces.move_set(self):

                xi,yi = move
                if xi == x and yi == y:
                    print("in CHeck")
                    return True
        return False

    def will_king_be_in_check(self,x,y):
        for pieces in self.playerOnePieces:
            for move in pieces.move_set(self):

                xi,yi = move
                if xi == x and yi == y:
                    print("will be in CHeck")
                    return True
        return False
    def is_checkmate(self):

        x, y = self.get_player_piece_location_on_board(21)
        king_piece = self.get_player_piece_at_location(x, y)
        moves = king_piece.move_set(self)
        spots_taken = []
        if self.is_king_in_check():
            # look at every move the king can make and see if an opp piece has a path to it

            for move in moves:

                x,y = move
                for pieces in self.playerOnePieces:
                    for movep in pieces.move_set(self):
                        xi,yi = movep
                        if xi == x and yi == y:
                            if move not in spots_taken:
                                spots_taken.append(move)

            if len(spots_taken) == len(moves):
                return True
            else:
                return False

    def get_player_piece_location_on_board(self, pie):
        for x in self.playerTwoPieces:
            if x.num == pie:
                return x.x, x.y

        for x in self.playerOnePieces:
            if x.num == pie:
                return x.x, x.y

    def get_player_two_pieces_nums(self):

        list_of_nums = []

        if not self.is_king_in_check():

            for x in self.playerTwoPieces:

                if len(x.move_set(self)) > 0:
                    list_of_nums.append(x.num)
        if self.is_king_in_check():
            list_of_nums.append(21)
        return list_of_nums

    def find_best_move(self, x, y,nnSuggested):
        piece_being_moved = self.get_player_piece_at_location(x, y)
        piece_move_set = piece_being_moved.move_set(self)
        print(piece_move_set)
        score = []
        print("cycle through movesets")
        num = 0

        sx,sy = get_xy_from_position(nnSuggested)

        if len(piece_move_set) > 1:

            for x in piece_move_set:
                intial_score = 100 / len(piece_move_set)
                print("getting score")
                temp_score = self.get_score_for_move(intial_score, x)
                if sx == x[0] and sy == x[1]:
                    temp_score+=1000
                    print('adding score to list')
                score.append(temp_score)
            i = 0

            inte = 0
            print(score)
            for sc in score:

                if sc > i:
                    i = sc
                    num = inte
                inte += 1
                print(num)
        print(piece_move_set[num])

        return piece_move_set[num]

    def get_score_for_move(self, intial_score, x):
        score = intial_score
        print(x[0],x[1])
        print(x[0], x[0])
        if self.is_opponent_piece_at_location(x[0], x[1]):
            oppPiece = self.get_opponent_piece_at_location(x[0], x[1])
            if oppPiece.piece_type == 'PAWN':
                score += 5
            elif oppPiece.piece_type == 'CASTLE':
                score += 7
            elif oppPiece.piece_type == 'HORSE':
                score += 10
            elif oppPiece.piece_type == 'SILVER':
                score += 20
            elif oppPiece.piece_type == 'GOLD':
                score += 30
            elif oppPiece.piece_type == 'Bishop' or oppPiece.piece_type == 'ROOK':
                score += 100
            elif oppPiece.piece_type == 'KING':
                score += 1000

        return score


def build_board(piecesOne, xOne, yOne, piecesTwo, xTwo, yTwo, promotelist):
    playerOnePieces = []
    playerTwoPieces = []
    for (pieceNum, x, y) in zip(piecesOne, xOne, yOne):
        playerOnePieces.append(piece.PieceFactory(pieceNum, x, y, False))
    for (pieceNum, x, y) in zip(piecesTwo, xTwo, yTwo):
        playerTwoPieces.append(piece.PieceFactory(pieceNum, x, y, True))

    return playerOnePieces, playerTwoPieces, promotelist


def get_xy_from_position(pos):
    return int(pos % 9 + 1), int(pos / 9 + 1)


def get_pos_from_xy(x, y):
    return x * 9 + y


def get_board(piecesOne, xOne, yOne, piecesTwo, xTwo, yTwo, promotelist):
    return board(piecesOne, xOne, yOne, piecesTwo, xTwo, yTwo, promotelist)


def get_list_of_move_set_as_positions(move_set):
    list_of_pos = []
    for x in move_set:
        list_of_pos.append(get_pos_from_xy(x[0], x[1]))
    return list_of_pos

