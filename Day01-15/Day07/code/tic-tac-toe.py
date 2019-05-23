"""
井字棋游戏

Version: 0.2
Author: 骆昊
Date: 2019-05-23
"""

import os



def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def is_winner(board, turn):
    """
    判断走棋者是否是赢家

    :param board: 当前棋盘数据
    :param turn: 走棋者
    :return 走棋者是赢家返回 True，否则返回 False
    """
    return ((board['TL'] == turn and board['TM'] == turn and board['TR'] == turn) or
    (board['ML'] == turn and board['MM'] == turn and board['MR'] == turn) or
    (board['BL'] == turn and board['BM'] == turn and board['BR'] == turn) or
    (board['TL'] == turn and board['ML'] == turn and board['BL'] == turn) or
    (board['TM'] == turn and board['MM'] == turn and board['BM'] == turn) or
    (board['TR'] == turn and board['MR'] == turn and board['BR'] == turn) or
    (board['TL'] == turn and board['MM'] == turn and board['BR'] == turn) or
    (board['BL'] == turn and board['MM'] == turn and board['TR'] == turn))


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if is_winner(curr_board, turn):
                    print("产生赢家：%s 赢得胜利" % turn)
                    break
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
