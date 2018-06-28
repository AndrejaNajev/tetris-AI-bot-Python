from bot_ import Bot
import position_
import field_
import copy

class Simulate():
    def __init__(self):
        self.cnt_moves=0
        self.cnt_cleared_lines=0
        self.round=0
        self.score=0
        self.combo=0
    
    def runGame(self):
        bot=Bot()
        field=copy.deepcopy(field_.pos.field)
        print 'Current piece: ', field_.pos.currentPiece
        print 'Next piece:', field_.pos.nextPiece
        while True:
            try:
                moves=bot.build_tree2(field_.pos, field_.pos.currentPiece)
                best_position=bot.evaluate_pos(moves,bot, field_.pos, field_.pos.currentPiece)
                action_moves=bot.get_moves(best_position, bot)
                move=position_.Position(field_.pos, field_.pos.currentPiece, field_.pos.nextPiece)
                field_.pos.prot=best_position[0]
                clears=move.from_tree_node(best_position)
                if clears==2:
                    self.score+=3
                    if self.combo>0:
                        self.combo+=1
                        self.score=self.score+self.combo-1
                    else:
                        self.combo+=1
                elif clears==3:
                    self.score+=6
                    if self.combo>0:
                        self.combo+=1
                        self.score=self.score+self.combo-1
                    else:
                        self.combo+=1
                elif clears==4:
                    self.score+=10
                    if self.combo>0:
                        self.combo+=1
                        self.score=self.score+self.combo-1
                    else:
                        self.combo+=1
                else:
                    self.combo=0
                field_.pos.print_pos()
                print 'Best position', best_position, 'Action moves', action_moves
                field_.pos.currentPiece=move.nextPiece
                field_.pos.nextPiece=field_.pos.getNextPiece() 
                self.cnt_moves+=1
                self.cnt_cleared_lines+=clears
                self.round+=1
                if self.round==15:
                    field_.pos.insert_row()
                    self.round=0
                else:
                    pass
            except IndexError:
                field_.pos.field=field
                print 'score', self.score
                print 'combo', self.combo
                return self.cnt_moves, self.cnt_cleared_lines
                    
#Simulate().runGame()      

