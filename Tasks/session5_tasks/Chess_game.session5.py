class Piece:
    def __init__(self, name, cord, color, points):
        self.name= name
        self.cord= cord
        self.color= color
        self.points= points

    def eat(self):
        print("eat")

    def die(self):
        print("die")
    
class Hourse(Piece):
    def __init__(self, name, cord, color, points, start_point):
        self.start_point = start_point
        super().__init__(name, cord, color, points)

    def move(self, start_ponit, end_point, board):
        start_x, start_y = start_ponit.split(",")
        end_x, end_y = end_point.split(",")
        x = ['-1,-2','-1,2', '1,2', '1,-2', '2,1', '-2,1', '2,-1', '-2,-1']
        f_string = f"{int(start_x) - int(end_x)},{int(start_y) - int(end_y)}"

        if f_string in x:
            board.map[end_point] = board.map[start_ponit]
            board.map[start_ponit] = ''
            return board
        else:
            return False


class Pawn(Piece):
    def __init__(self, name, cord, color, points, start_point):
        self.start_point =start_point
        super().__init__(name, cord, color, points)

    def move(self, start_ponit, end_point, board):
        start_x, start_y = start_ponit.split(",")
        end_x, end_y = end_point.split(",")
        x = ['0,1','-1,0']
        f_string = f"{int(start_x) - int(end_x)},{int(start_y) - int(end_y)}"
        #x_enemy = ['1,-1','2,-2','-2,-1','1,1','-1,1','-1,0'] # for eating  

        if f_string in x:
            if Piece.color != board.map[end_point].color:
               Piece.eat()
               board.map[end_point] = board.map[start_ponit]
               board.map[start_ponit] = ''
               return board
        else:
            print("You Can not pass over your piece")
            return False
        

class Rook(Piece):
    def __init__(self, name, cord, color, points, start_point):
        self.start_point =start_point
        super().__init__(name, cord, color, points)

    def move(self, start_ponit, end_point, board):
        start_x, start_y = start_ponit.split(",")
        end_x, end_y = end_point.split(",")
        x = ['0,1','0,2','1,0','2,0','0,-1','0,-2','-1,0','-2,0']
        f_string = f"{int(start_x) - int(end_x)} , {int(start_y) - int(end_y)}"
        if f_string in x:
            if Piece.color != board.map[end_point].color:
                Piece.eat()
                board.map[end_point] = board.map[start_ponit]
                board.map[start_ponit] = ''
                return board
        else:
            print("You Can not pass over your piece")
            return False
        ## TODO: add the logic of eating

class Bishop(Piece):
    def __init__(self, name, cord, color, points, start_point):
        self.start_point =start_point
        super().__init__(name, cord, color, points)

    def move(self, start_ponit, end_point, board):
        start_x, start_y = start_ponit.split(",")
        end_x, end_y = end_point.split(",")
        if abs(int(start_x) - int(end_x)) == abs(int(start_y) - int(end_y)):
            board.map[end_point] = board.map[start_ponit]
            board.map[start_ponit] = ''
            return board
        else:
            return False


class King(Piece):
    def __init__(self, name, cord, color, points, start_point):
        self.start_point =start_point
        super().__init__(name, cord, color, points)

    def move(self, start_ponit, end_point, board):
        start_x, start_y = start_ponit.split(",")
        end_x, end_y = end_point.split(",")
        if abs(int(start_x) - int(end_x)) <= 1 and abs(int(start_y) - int(end_y)) <= 1:
            board.map[end_point] = board.map[start_ponit]
            board.map[start_ponit] = ''
            return board
        else:
            return False
        

class Queen(Piece):
    def __init__(self, name, cord, color, points, start_point):
        self.start_point =start_point
        super().__init__(name, cord, color, points)

    def move(self, start_ponit, end_point, board):
        start_x, start_y = start_ponit.split(",")
        end_x, end_y = end_point.split(",")
        if abs(int(start_x) - int(end_x)) == abs(int(start_y) - int(end_y)) or (int(start_x) == int(end_x) or int(start_y) == int(end_y)):
            board.map[end_point] = board.map[start_ponit]
            board.map[start_ponit] = ''
            return board
        else:
            return False









class Board:
    def __init__(self, num_block, map):
        self.map = map
        self.num_block = num_block

    def is_empty(self, cord):
        if self.map[cord] == '':
            return True
        else:
            return ("This position is not empty")

    def get_piece_color(self, cord):
        return self.map[cord].color
    
    def get_piece(self, cord):
        return self.map[cord]


class Players:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Game:
    def __init__(self, player1, player2, board, score):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.score = score

    def check_board(self, point):
        return self.board.map[point]

    def draw_board(self):
        # Draws all pieces on the board, including empty squares
        print(" " + " ".join([str(i) for i in range(8)]))
        for row in range(8):
            row_str = f"{row}  "
            for col in range(8):
                cord = f"{row},{col}"
                piece = self.board.map.get(cord, '')
                if piece == '' or piece is None:
                    row_str += " . "
                else:
                    # Use first letter of piece name and color initial
                    row_str += f"{piece.name[0]}{piece.color[0]} "
            print(row_str)

    def start_game(self):
        print("%s is playing with %s"%(self.player1.name, self.player1.color))
        print("%s is playing with %s"%(self.player2.name, self.player2.color))
        player_on_turn = player1
    
    
        
        while(True):
            self.draw_board()
            player_input = input(f"{player_on_turn.name} Enter your cord: ")
            start_point, end_point = player_input.split(" ")
            if not self.board.is_empty(start_point) and \
            self.board.get_piece_color(start_point) == player_on_turn.color:
                if self.board.is_empty(end_point) or \
                (not self.board.is_empty(end_point) and self.board.get_piece_color(end_point) != player_on_turn.color):
                    captured_piece = self.board.get_piece(end_point)
                    current_piece = self.board.get_piece(start_point)
                    #if end_point == "0,3" or "7,3" and \  (((this is was expected to be for check the king but it has failed i cant make it work i dont even what is the wring with it))) 
                    #self.board.get_piece_color(end_point) != player_on_turn.color:
                        # print(f"{player_on_turn} has won and your king is checked")
                         
                    if captured_piece:
                            print(f"{player_on_turn.name}'s {current_piece.name} ({current_piece.color}) captured {captured_piece.name} ({captured_piece.color}) at {end_point}!")
                    
                            result = current_piece.move(start_point, end_point, self.board)
                            if result:
                                self.board = result
                                if player_on_turn == player1:
                                    player_on_turn = player2
                                else:
                                    player_on_turn = player1
                            else: pass
                    else: 
                            print("Invalid Move!")
                    #else: 
                        #pass           

                else:
                    print("cant move on your pieces")
            else:
                print("Wrong Cord")


            start_point_peiece = self.check_board(start_point)
            end_point_peiece = self.check_board(end_point)
            if start_point_peiece:
                if start_point_peiece.color == player_on_turn.color:
                    if end_point_peiece or end_point_peiece != player_on_turn.color:
                        self.board.map[end_point] = self.board.map[start_point]

                        self.board.map[start_point] = ''






map = {
    "0,0": Rook(color='White',start_point="0,0",name='Rook1',points=5,cord="0,0"), ## TODO: add Rook here
    "0,1": Hourse(color='White',start_point="0,1",name='Hourse1',points=3,cord="0,1"),
    "0,2": Bishop(color='White',start_point="0,2",name='Bishop1',points=3,cord="0,2"),
    "0,3": King(color='White',start_point="0,3",name='King',points=0,cord="0,3"),
    "0,4": Queen(color='White',start_point="0,4",name='Queen',points=9,cord="0,4"),
    "0,5": Bishop(color='White',start_point="0,6",name='Bishop1',points=3,cord="0,6"),
    "0,6": Hourse(color='White',start_point="0,7",name='Hourse1',points=3,cord="0,7"),
    "0,7": Rook(color='White',start_point="0,7",name='Rook1',points=5,cord="0,7"), ## TODO: add Rook here
    "1,1": Pawn(color='White',start_point="1,1",name='Pawn1',points=1,cord="1,1"), ## TODO: add Pawm here
    "1,2": Pawn(color='White',start_point="1,2",name='Pawn1',points=1,cord="1,2"), ## TODO: add Pawm here
    "1,3": Pawn(color='White',start_point="1,3",name='Pawn1',points=1,cord="1,3"), ## TODO: add Pawm here
    "1,0": Pawn(color='White',start_point="1,0",name='Pawn1',points=1,cord="1,0"), ## TODO: add Pawm here
    "1,4": Pawn(color='White',start_point="1,4",name='Pawn1',points=1,cord="1,4"), ## TODO: add Pawm here
    "1,5": Pawn(color='White',start_point="1,5",name='Pawn1',points=1,cord="1,5"), ## TODO: add Pawm here
    "1,6": Pawn(color='White',start_point="1,6",name='Pawn1',points=1,cord="1,6"), ## TODO: add Pawm here
    "1,7": Pawn(color='White',start_point="1,7",name='Pawn1',points=1,cord="1,7"), ## TODO: add Pawm here
    "2,0": '',
    "2,1": '',
    "2,2": '',
    "2,3": '',
    "2,4": '',
    "2,5": '',
    "2,6": '',
    "2,7": '',
    "3,0": '',
    "3,1": '',
    "3,2": '',
    "3,3": '',
    "3,4": '',
    "3,5": '',
    "3,6": '',
    "3,7": '',
    "4,0": '',
    "4,1": '',
    "4,2": '',
    "4,3": '',
    "4,4": '',
    "4,5": '',
    "4,6": '',
    "4,7": '',
    "5,0": '',
    "5,1": '',
    "5,2": '',
    "5,3": '',
    "5,4": '',
    "5,5": '',
    "5,6": '',
    "5,7": '',
    "6,0": Pawn(color='Black',start_point="6,0",name='Pawn1',points=1,cord="6,0"), ## TODO: add Pawn here
    "6,1": Pawn(color='Black',start_point="6,1",name='Pawn1',points=1,cord="6,1"), ## TODO: add Pawn here
    "6,2": Pawn(color='Black',start_point="6,2",name='Pawn1',points=1,cord="6,2"), ## TODO: add Pawn here
    "6,3": Pawn(color='Black',start_point="6,3",name='Pawn1',points=1,cord="6,3"), ## TODO: add Pawn here
    "6,4": Pawn(color='Black',start_point="6,4",name='Pawn1',points=1,cord="6,4"), ## TODO: add Pawn here
    "6,5": Pawn(color='Black',start_point="6,5",name='Pawn1',points=1,cord="6,5"), ## TODO: add Pawn here
    "6,6": Pawn(color='Black',start_point="6,6",name='Pawn1',points=1,cord="6,6"), ## TODO: add Pawn here
    "6,7": Pawn(color='Black',start_point="6,7",name='Pawn1',points=1,cord="6,7"), ## TODO: add Pawn here
    "7,0": Rook(color='Black',start_point="7,0",name='Rook1',points=5,cord="7,0"), ## TODO: add Rook here
    "7,1": Hourse(color='Black', start_point="7,1", name='Hourse1', points=3,cord="7,1"),
    "7,2": Bishop(color='Black', start_point="7,2", name='Bishop1', points=3,cord="7,2"),
    "7,3": King(color='Black', start_point="7,3", name='King', points=0,cord="7,3"),
    "7,4": Queen(color='Black', start_point="7,4", name='Queen', points=9,cord="7,4"),
    "7,5": Bishop(color='Black', start_point="7,5", name='Bishop1', points=3,cord="7,5"),
    "7,6": Hourse(color='Black', start_point="7,7", name='Hourse1', points=3,cord="7,7"),
    "7,7": Rook(color='Black',start_point="7,0",name='Rook1',points=5,cord="7,0"), ## TODO: add Rook here
    }



chess_board = Board(num_block=64, map=map)
player1 = Players(name='mofasa', color='White')
player2 = Players(name='bomba', color="Black")

game1 = Game(player1=player1,player2=player2,board=chess_board,score=0).start_game()