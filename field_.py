import random

tetris_shapes = {
    'I': [[[0, 0, 0, 0],
           [1, 1, 1, 1],
           [0, 0, 0, 0],
           [0, 0, 0, 0]],

          [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 1, 0]],

          [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [1, 1, 1, 1],
           [0, 0, 0, 0]],

          [[0, 1, 0, 0],
           [0, 1, 0, 0],
           [0, 1, 0, 0],
           [0, 1, 0, 0]]],

    'J': [[[1, 0, 0],
           [1, 1, 1],
           [0, 0, 0]],

          [[0, 1, 1],
           [0, 1, 0],
           [0, 1, 0]],

          [[0, 0, 0],
           [1, 1, 1],
           [0, 0, 1]],

          [[0, 1, 0],
           [0, 1, 0],
           [1, 1, 0]]],

    'L': [[[0, 0, 1],
           [1, 1, 1],
           [0, 0, 0]],

          [[0, 1, 0],
           [0, 1, 0],
           [0, 1, 1]],

          [[0, 0, 0],
           [1, 1, 1],
           [1, 0, 0]],

          [[1, 1, 0],
           [0, 1, 0],
           [0, 1, 0]]],

    'O':  [[[1, 1],
            [1, 1]]],

    'S': [[[0, 1, 1],
           [1, 1, 0],
           [0, 0, 0]],

          [[0, 1, 0],
           [0, 1, 1],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 1, 1],
           [1, 1, 0]],

          [[1, 0, 0],
           [1, 1, 0],
           [0, 1, 0]]],

    'T': [[[0, 1, 0],
           [1, 1, 1],
           [0, 0, 0]],

          [[0, 1, 0],
           [0, 1, 1],
           [0, 1, 0]],

          [[0, 0, 0],
           [1, 1, 1],
           [0, 1, 0]],

          [[0, 1, 0],
           [1, 1, 0],
           [0, 1, 0]]],

    'Z': [[[1, 1, 0],
           [0, 1, 1],
           [0, 0, 0]],

          [[0, 0, 1],
           [0, 1, 1],
           [0, 1, 0]],

          [[0, 0, 0],
           [1, 1, 0],
           [0, 1, 1]],

          [[0, 1, 0],
           [1, 1, 0],
           [1, 0, 0]]]
}


class Field:
    def __init__(self, fstr):
        self.height, self.width = 20, 10
        self.px, self.py = 0, 0
        self.currentPiece = random.choice(tetris_shapes.keys())
        self.nextPiece = random.choice(tetris_shapes.keys())
        self.prot = 0
        self.field = []
        self.final = None
        self.parent = None
        self.hash = self.prot, self.px, self.py, self.final
        for i, row in enumerate(fstr.split(';')):
            r = []
            for j, col in enumerate(row.split(',')):
                col = int(col)
                r.append(col)
            self.field.append(r)

    def print_pos(self):
        for r in range(20):
            print self.field[r]

    def size(self):
        return self.width, self.height

    def updateField(self, field):
        self.field = field

    def fit_piece(self, pmask, px, py):
        block = tetris_shapes[pmask][self.prot]
        for j, row in enumerate(block):
            for i, val in enumerate(row):
                if val == 1:
                    val = 2
                    self.field[j + py][i + px] += val
        return self.field

    def drop(self, pmask, px, py):
        while pos.fits(pmask, px, py) == False:
            py += 1
            self.py += 1
        self.py -= 1
        return self.py

    def fits(self, pmask, px, py):
        block = tetris_shapes[pmask][self.prot]
        for j, row in enumerate(block):
            for i, cell in enumerate(row):
                try:
                    if cell and self.field[j + py][i + px]:
                        return True
                except IndexError:
                    return True
        return False

    def getNextPiece(self):
        self.nextPiece = random.choice(tetris_shapes.keys())
        return self.nextPiece

    def getCurrentPiece(self):
        return self.currentPiece

    def getField(self):
        return self.field

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getProt(self):
        return self.prot

    def turnright(self):
        if self.currentPiece == 'O' or self.prot == 3:
            self.prot = 0
        else:
            self.prot += 1
        return self.prot

    def turnleft(self):
        if self.currentPiece == 'O':
            self.prot = 0
        elif self.prot == 0:
            self.prot = 3
        else:
            self.prot -= 1
        return self.prot

    def left(self):
        if self.px == 0:
            return self.px
        else:
            self.px -= 1
            return self.px

    def right(self):
        self.px += 1
        return self.px

    def down(self):
        self.py += 1
        return self.py

    def insert_row(self):
        del(self.field[0])
        self.field.insert(19, [3 for x in range(pos.getWidth())])
        return self.field


pos = Field("0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0; 0,0,0,0,0,0,0,0,0,0")
