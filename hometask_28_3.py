
def count_moves(count, n, start, via, finish):
    move = count
    if n > 0:
        move = count_moves(move, n-1, start, finish, via)
        print(f'Moving from {start} to {finish}')
        move = move + 1
        move = count_moves(move, n-1, via, start, finish)
    return move


print(count_moves(0, 5, 'A', 'B', 'C'))
