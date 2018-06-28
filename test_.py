from simulate_ import Simulate


class Test():

    def __init__(self):
        self.avg_moves = 0
        self.avg_cl_lines = 0

    def play(self, n):
        for game in range(n):
            print 'GAME: ', game
            a = Simulate().runGame()
            self.avg_moves += a[0]
            self.avg_cl_lines += a[1]
        self.avg_moves = self.avg_moves / n
        print "NUMBER OF GAMES PLAYED: ", n
        print 'Average number of moves: ', self.avg_moves
        self.avg_cl_lines = self.avg_cl_lines / n
        print 'Average number of cleared lines: ', self.avg_cl_lines


play_tetris = Test()
n = int(input("Enter a number n: "))
play_tetris.play(n)
