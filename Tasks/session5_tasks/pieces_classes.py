
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
        self.start_point =start_point
        super().__init__(name, cord, color, points)

    def move(self, start_ponit, end_point, board):
        start_x, start_y = start_ponit.split(",")
        end_x, end_y = end_point.split(",")
        x = ['-1,-2','-1,2', '1,2', '1,-2', '2,1', '-2,1', '2,-1', '-2,-1']
        f_string = f"{int(start_x)-int(end_x)},{int(start_y) - int(end_y)}"

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
        
        ## TODO: add the logic of eating


class Rook(Piece):
    def __init__(self, name, cord, color, points, start_point):
        self.start_point =start_point
        super().__init__(name, cord, color, points)

    def move(self, start_ponit, end_point, board):
        start_x, start_y = start_ponit.split(",")
        end_x, end_y = end_point.split(",")
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