from fileinput import filename
from nbformat import read
import numpy as np
import chess 
import chess.pgn
import chess.svg
import chess.engine
import tkinter as tk
from show_svg import showimg, delete_item, insertfiles

from pgn_to_custom_format import read_single_game, test_single_game


#pgn_path = open("/home/matz/Downloads/best_2000/ficsgamesdb_2000_standard2000_nomovetimes_247194.pgn")

def chess_plot (pgn_path):
        print(pgn_path)
        pgn_file = open(pgn_path)
        game = chess.pgn.read_game(pgn_file)
        board = game.board()
        fen_data = board.fen()
        fen_board = fen_data.split()[0] 
        move_number = 0
        
        for move in game.mainline_moves():
                board.push(move)
                fen_data = board.fen()
                fen_board = fen_data.split()[0]
                
                #print('render'+ str(move) +'.svg')
                
                move_number += 1
                
                
                with open('./images/'+'render'+ f'{move_number:03}' + '.svg', 'w+') as f:
                        f.write( chess.svg.board( 
                                chess.Board(fen_board)
                        ))  
        root = tk.Tk()
        
        insertfiles()
       
        
        root.mainloop()         
      
    
        





