
class Players:
    def __init__(self, name, start):
        self.name=name
        self.start = start

    def tell_me_your_start(self):
        return self.start
    

class TikTak:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.map = {'0,0':'','1,0':'','2,0':'','0,1':'','0,2':'','1,1':'','1,2':'','2,1':'','2,2':''}

        self.turn = 1

    def how_is_playing(self):
        print(f"Current turn: {self.turn}")
        print(f"{self.player1.name} (X) vs {self.player2.name} (O)")

    def draw_map(self):
        print("0 | 1 | 2 "
                "\n---------"
                f"\n0 | {self.map['0,0']} | {self.map['1,0']} | {self.map['2,0']}"
                "\n---------"
                f"\n1 | {self.map['0,1']} | {self.map['1,1']} | {self.map['2,1']}"
                "\n---------"
                f"\n2 | {self.map['0,2']} | {self.map['1,2']} | {self.map['2,2']}")

    def check_winner(self):
        winning_combinations = [
            ['0,0', '0,1', '0,2'],  # Row 1
            ['1,0', '1,1', '1,2'],  # Row 2
            ['2,0', '2,1', '2,2'],  # Row 3
            ['0,0', '1,0', '2,0'],  # Column 1
            ['0,1', '1,1', '2,1'],  # Column 2
            ['0,2', '1,2', '2,2'],  # Column 3
            ['0,0', '1,1', '2,2'],  # Diagonal
            ['0,2', '1,1', '2,0'],  # Diagonal
        ]

        for combo in winning_combinations:
            ## Check if all positions in the winning combination have the same value
            ## ex: if self.map[combo[0]] == self.map[combo[1]] == self.map[combo[2]] != '' >> all X or all O but not all ''
            if self.map[combo[0]] == self.map[combo[1]] == self.map[combo[2]] != '':
                return self.map[combo[0]]
        return None

    def play(self):
        while True:
            player_on_turn = ''
            if self.turn == 1:
                player_on_turn = self.player1
            else:
                player_on_turn = self.player2

            self.draw_map()
            winner = self.check_winner()
            ## if some one wins, winner = X or O
            ## else it will be None
            if winner:
                self.draw_map()
                ## TODO : handle winning and end the game 


            while True:
                cord = input(f"{player_on_turn.name}: Enter your next move: ")

                ## self.map.keys() >> ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']
                if cord in self.map.keys():
                    ## self.map[cord] >> X or O or ''
                    if self.map[cord] == '': ## if empty
                        ## player_on_turn.start >> X or O
                        self.map[cord] = player_on_turn.start 
                        ## change turn
                        ## TODO : handle turn change

                        break
                    else:
                        print("invalid")
                else:
                        print("invalid, enter valid  cord")

    def print_winner(self):
        ## TODO: print the winner name
        pass


player1 = Players(name='timon', start= 'X')
player2 = Players(name='bomba', start= 'O')

TikTak(player1=player1, player2=player2).play()