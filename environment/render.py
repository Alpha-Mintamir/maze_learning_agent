def print_maze(maze):
    symbols = {0: '.', 1: 'X', 2: 'S', 3: 'G'}
    for row in maze:
        print(' '.join(symbols[cell] for cell in row))
