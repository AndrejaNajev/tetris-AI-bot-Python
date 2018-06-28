import field_

class Treenode:
    def __init__(self):
         self.prot=None
         self.px=None
         self.py=None
         self.parent=None
         self.move=None
         self.final=None
         self.hash=None
        
    def from_pos(self,pos):
         self.prot=pos.prot
         self.px=pos.px
         self.py=pos.py
         return self.prot, self.px, self.py
        
    def child(self,pos,field, piece, m):
        self.prot, self.px, self.py=pos[0],pos[1], pos[2]
        self.parent=self.prot, self.px, self.py
        if m=='left':
            self.px= field.left()
            self.move='left'
            self.hash=self.prot, self.px,self.py
            return self.hash
        elif m=='right':
            self.px= field.right()
            self.move='right'
            self.hash=self.prot, self.px,self.py
            return self.hash
        elif m=='turnleft':
            self.prot= field.turnleft()  
            self.move='turnleft'
            self.hash=self.prot, self.px,self.py
            return self.hash
        elif m=='turnright':
            self.prot= field.turnright()
            self.move='turnright'
            self.hash=self.prot, self.px,self.py
            return self.hash
        elif m=='down':
            self.py=field.down()
            self.move='down'
            self.hash=self.prot, self.px, self.py
            return self.hash
        elif m=='drop':
            self.final=True
            self.move='drop'
            self.py= field.drop(piece, self.px,self.py)
            self.hash=self.prot, self.px,self.py
            return self.hash
            
    def is_legal(self,pos, field, piece):
        block=field_.tetris_shapes[piece][pos[0]]
        for y, row in enumerate(block):
            for x, cell in enumerate(row):
                try:
                    if cell and field.field[y + pos[2]][x + pos[1] ]:
                        return True
                except IndexError:
                    return True
        return False

treenode=Treenode()

