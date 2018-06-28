import field_

class Position():
    
    def __init__(self, field, piece, nextPiece):
        self.field = field
        self.currentPiece = piece
        self.nextPiece = nextPiece
            
    def copy(self):
        position = Position(self.field, self.currentPiece, self.nextPiece)
        return position.field, position.currentPiece, position.nextPiece
    
    def from_tree_node(self,node):
         self.newInstance=self.copy()  
         self.field=self.newInstance[0]
         self.currentPiece=self.newInstance[1]
         self.nextPiece=self.newInstance[2]
         self.field=self.field.fit_piece(self.currentPiece, node[1], node[2])
         clears = 0
         for y in xrange(field_.pos.getHeight()):
            if all(map(lambda x: x == 2, self.field[y])):
                del(self.field[y])
                self.field.insert(0, [0 for x in range(field_.pos.getWidth())])
                clears += 1
         return clears
