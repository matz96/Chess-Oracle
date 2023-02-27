import chess
import chess.pgn
import numpy as np


def test_single_game():
    pgn_file = open(
        "C:\\Users\\Daniel Richner\\OneDrive - FHNW\\ML_Projekt\\best_2000\\ficsgamesdb_2021_standard2000_nomovetimes_247238.pgn")

    moves = list()
    for i in range(0, 5):
        game = chess.pgn.read_game(pgn_file)
        for move in read_single_game(game):
            moves.append(move)
    return moves


def read_pgn_files(paths):
    moves = list()
    for path in paths:
        moves.extend(read_pgn_file(path))
    return moves


def read_pgn_files_min_move_number(paths, min_move_number):
    moves = list()
    for path in paths:
        moves.extend(read_pgn_file_min_move_number(path, min_move_number))
    return moves


def read_pgn_file(path):
    pgn_file = open(path)

    moves = list()
    game = chess.pgn.read_game(pgn_file)

    while game != None:
        moves.extend(read_single_game(game))

        game = chess.pgn.read_game(pgn_file)

    return moves


def read_pgn_file_min_move_number(path, min_move_number):
    pgn_file = open(path)

    moves = list()
    game = chess.pgn.read_game(pgn_file)

    while game != None:
        moves.extend(read_single_game_min_move_number(game, min_move_number))

        game = chess.pgn.read_game(pgn_file)

    return moves


def read_single_game(game):
    move_flattened = list()
    board = game.board()

    game_result = parse_game_result_header(game.headers["Result"])
    fen_data = board.fen()
    fen_board = fen_data.split()[0]

    move_number = 0
    move_flattened.append(
        (game_result, move_number, read_single_move(fen_board)))
    for move in game.mainline_moves():
        board.push(move)
        move_number += 1
        fen_data = board.fen()
        fen_board = fen_data.split()[0]
        move_flattened.append(
            (game_result, move_number, read_single_move(fen_board)))
    return move_flattened


def read_single_game_min_move_number(game, min_move_number):
    move_flattened = list()
    board = game.board()

    game_result = parse_game_result_header(game.headers["Result"])
    fen_data = board.fen()
    fen_board = fen_data.split()[0]

    move_number = 0

    for move in game.mainline_moves():
        board.push(move)
        move_number += 1

        if move_number >= min_move_number:
            fen_data = board.fen()
            fen_board = fen_data.split()[0]
            move_flattened.append(
                (game_result, move_number, read_single_move(fen_board)))
    return move_flattened


def parse_game_result_header(game_result_raw):
    # arr[0] -> white_wins
    # arr[1] -> black_wins
    # arr[2] -> draw
    arr = np.zeros((3), dtype=bool)
    if game_result_raw.startswith('1/2'):
        arr[0] = False
        arr[1] = False
        arr[2] = True
    elif game_result_raw.startswith('1'):
        arr[0] = True
        arr[1] = False
        arr[2] = False
    elif game_result_raw.startswith('0'):
        arr[0] = False
        arr[1] = True
        arr[2] = False
    else:
        raise Exception()

    return arr


figure_to_array_position = {
    "R": 0,
    "N": 1,
    "B": 2,
    "Q": 3,
    "K": 4,
    "P": 5,
    "r": 6,
    "n": 7,
    "b": 8,
    "q": 9,
    "k": 10,
    "p": 11
}


def read_single_move(fen_board):
    export_array = np.zeros((12), dtype=np.float32)

    position = 0

    for character in fen_board:
        if character in figure_to_array_position:
            figure_position = figure_to_array_position[character]
            export_array[figure_position] = export_array[figure_position] + 1.0
            position = position + 1

    return export_array
