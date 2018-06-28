import treenode_
import field_
import copy
from sys import stdin, stdout
from game_ import Game
from main import Main

class Bot:

    def __init__(self):
        self._game = Game()
        self._main = Main(self._game)
        
    def evaluate_pos(self,pos,bot, field, piece):
        list_aggr=[]
        a = -0.510066
        b = 0.760666
        c = -0.35663
        d = -0.184483
        for i in pos:
            aggr = bot.aggregate_height(i,bot, field, piece)
            comp = bot.complete_lines(i,bot, field, piece)
            hole = bot.holes(i,bot, field, piece)
            bump = bot.bumpiness(i,bot, field, piece)
            best_pos = (a*aggr)+(b*comp)+(c*hole)+(d*bump)
            list_aggr.append(best_pos)        
        max_value = max(list_aggr)
        max_value_index = list_aggr.index(max_value)
        best_pos = pos[max_value_index]
        return best_pos
            
    def aggregate_height(self, i,bot, field, piece):
        parent_field = copy.deepcopy(field.field)
        prot, px, py = i[0], i[1], i[2]
        block = field_.tetris_shapes[piece][prot]
        for j, row in enumerate(block):
            for i, val in enumerate(row):
                if val == 1:
                    val = 2
                    parent_field[j+py][i+px] += val
        col_cnt = []
        height_counter = 0
        total = 0
        for i in range(0,10):
            col = [x[i] for x in parent_field]
            for row, cell in enumerate(col):
                if bot._is_block(cell) and cell == 2:
                    height_counter += (20-row)
                    total += height_counter
                    break;
            col_cnt.append(height_counter)
            height_counter = 0
        return total
        
    def complete_lines(self, i,bot, field, piece):
        parent_field = copy.deepcopy(field.field)
        prot, px, py = i[0], i[1], i[2]
        block = field_.tetris_shapes[piece][prot]
        for j, row in enumerate(block):
            for i, val in enumerate(row):
                if val == 1:
                    val = 2
                    parent_field[j+py][i+px] += val
        complete_lines = 0
        for y in xrange(0,20):
            if all(map(lambda x: x == 2, parent_field[y])):
                complete_lines +=1
        return complete_lines
                
    def _is_block(self,cell):
	return cell != 0 

    def _is_empty(self,cell):
	return cell == 0
        
    def holes(self,i,bot, field, piece):
        parent_field = copy.deepcopy(field.field)
        prot, px, py = i[0], i[1], i[2]
        block = field_.tetris_shapes[piece][prot]
        for j, row in enumerate(block):
            for i, val in enumerate(row):
                if val == 1:
                    val = 2
                    parent_field[j+py][i+px] += val
        holes = []
        hole_counter = 0
        block_in_col = False
        for x in range(len(parent_field[0])):
            for y in range(len(parent_field)):
                if block_in_col and bot._is_empty(parent_field[y][x]):
                    holes.append((x,y))
                    hole_counter += 1
                elif bot._is_block(parent_field[y][x]) and parent_field[y][x] == 2:
                    block_in_col = True
            block_in_col = False
        return hole_counter
                
    def bumpiness(self, i,bot, field, piece):
        parent_field = copy.deepcopy(field.field)
        prot, px, py = i[0], i[1], i[2]
        block = field_.tetris_shapes[piece][prot]
        for j, row in enumerate(block):
            for i, val in enumerate(row):
                if val == 1:
                    val = 2
                    parent_field[j+py][i+px] += val
        col_cnt = []
        block_counter = 0
        for i in range(0,10):
            col = [x[i] for x in parent_field]
            for row, cell in enumerate(col):
                if bot._is_block(cell) and cell == 2:
                    block_counter += (20-row)
                    break;
            col_cnt.append(block_counter)
            block_counter = 0
        bumpiness = abs(col_cnt[0]-col_cnt[1]) + abs(col_cnt[1]-col_cnt[2]) + abs(col_cnt[2]-col_cnt[3])+abs(col_cnt[3]-col_cnt[4])+abs(col_cnt[4]-col_cnt[5])+abs(col_cnt[5]-col_cnt[6])+abs(col_cnt[6]-col_cnt[7])+abs(col_cnt[7]-col_cnt[8])+abs(col_cnt[8]-col_cnt[9])
        return bumpiness
    
    def get_moves(self,best_position, bot):
        moves = []
        parent_prot, parent_px = 0, 3
        best_prot = best_position[0]
        best_px = best_position[1]
        if parent_prot > best_prot:
            for i in range(best_prot, parent_prot):
                moves.append('turnleft')
        else:
            for i in range(parent_prot, best_prot):
                moves.append('turnright')
        if parent_px > best_px:
            for i in range(best_px, parent_px):
                moves.append('left')
        else:
            for i in range(parent_px, best_px):
                moves.append('right')
        moves.append('drop')
        return moves
        
    
    def build_tree2(self, field, piece):
        lst_pos, lst_pos2, lst_pos3 = [], [], []
        final_list = []
        list_ = copy.deepcopy(final_list)
        position = copy.deepcopy(treenode_.treenode.from_pos(field))
        if piece =='O':
            lst_pos.append((0,0,0))
        else:
            for i in range(0,4):
                position = treenode_.treenode.child(position, field, piece,'turnright')
                if position not in lst_pos:
                    lst_pos.append((position[0], position[1], position[2]))
        for i in lst_pos:
            if (piece =='O' and i[0] == 0):
                for j in range(0,8):
                    i = treenode_.treenode.child(i, field, piece, 'right')
                    lst_pos2.append((i[0], i[1], i[2]))
                field.px=0
            elif (piece =='I' and i[0] == 0) or (piece == 'I' and i[0] == 2):
                for j in range(0,6):
                    i = treenode_.treenode.child(i, field, piece,'right')
                    lst_pos2.append((i[0], i[1], i[2]))
                field.px = 0
            elif (piece =='I' and i[0] == 1):
                for j in range(0,7):
                    i = treenode_.treenode.child(i,field, piece, 'right')
                    lst_pos2.append((i[0], i[1], i[2]))
                field.px=0
            elif (i[0] == 3):
                for j in range(0,8):
                    i = treenode_.treenode.child(i,field, piece, 'right')
                    lst_pos2.append((i[0], i[1], i[2]))
                field.px=0   
            else:
                for j in range(0,7):
                    i = treenode_.treenode.child(i,field, piece, 'right')
                    lst_pos2.append((i[0], i[1], i[2]))
                field.px=0
        lst_pos.extend(lst_pos2)  
        for position in lst_pos:
            while treenode_.treenode.is_legal(position,field, piece) == False:
                position = treenode_.treenode.child(position, field, piece, 'down')
                lst_pos3.append(position)
            del lst_pos3[-1]
            field.prot, field.px, field.py = 0, 0, 0
            final_list.append(lst_pos3[-1])
        final_list = sorted(final_list, reverse=False)
        list_ = final_list
        final_list = []
        return list_

    def run(self):
        while not stdin.closed:
            try:
                line = stdin.readline().strip()
                if len(line) == 0:
                    continue
                moves = self.interpret(line)
                if moves:
                    self.sendMoves(moves)
            except EOFError:
                return
   
    def interpret(self, line):
        if line.startswith('action'):
            bot=Bot() 
            moves=bot.build_tree2(self._game.me.field,self._game.currentPiece)            
            best_position= bot.evaluate_pos(moves,bot, self._game.me.field, self._game.currentPiece)
            best_prot=best_position[0]
            best_px=best_position[1]
            best_py=best_position[2]
            if self._game.currentPiece=='O':
                best_position=best_prot, best_px-1, best_py
            action_moves=bot.get_moves(best_position, bot)
            return action_moves
        else:
            self._main.parse(line)

    @staticmethod
    def sendMoves(moves):
        stdout.write(','.join(moves) + '\n')
        stdout.flush()
 
if __name__ == '__main__':
    Bot().run()  

