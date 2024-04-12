import numpy as np
from random import sample, randint
from copy import deepcopy
import annealer

def generate_sudoku(n,verbose=False):
    side = n * n
    
    block = sample(range(0, n), n)
    block_itr = sample(range(0, n), n)
    
    nums = sample(range(1, side + 1), side)
    
    sudoku = []
    for r in block:
        for c in block_itr:
            start = r + n * c
            
            grid_row = []
            for k in range(side):
                grid_row.append(nums[(start + k) % side])
                
            sudoku.append(grid_row)

    if verbose:
        print_grid(sudoku)
        
    return sudoku

def generate_puzzle(grid, n, verbose=False):
    temp_grid = deepcopy(grid)
    side = len(grid)
    
    if n >= side * side:
        raise ValueError(f"Cannot remove {n} elements from grid with {side * side} elements!")
    
    indices = np.random.choice(range(side * side), n, replace=False)
    
    for i in range(n):
        rows = indices[i] // side
        cols = indices[i] % side
        temp_grid[rows][cols] = 0
    
    if verbose:
        print_grid(temp_grid)
        
    return temp_grid

def get_block_indices(start, dim):
    return list(range(start, start + dim))

def validate_sudoku(puzzle):
    side = len(puzzle)
    dim = int(np.sqrt(side))
    
    sqr = 0
    sqc = 0
    for r in range(side):
        row = np.array(puzzle[r])
        column = np.array(puzzle)[:, [r]].transpose()[0]
        
        ri = get_block_indices(sqr, dim)
        ci = get_block_indices(sqc, dim)
        square = np.array(puzzle)[ri, :][:, ci].reshape(side)
        
        sqr = sqr + dim
        
        if sqr == side:
            sqr = 0
            sqc = sqc + dim
            
        for val in range(1, side + 1):
            if len(np.where(row == val)[0]) > 1 or len(np.where(column == val)[0]) > 1 or len(
                    np.where(square == val)[0]) > 1:
                return False
            
    return True

def print_grid(puzzle):
    side = len(puzzle)
    n = int(np.sqrt(side))
    
    factor = 2 * (n + 1) + (side - n) + (2 * 2 * side + side)
    
    print('-' * factor)
    for i in range(side): 
        temp = ''
        for j in range(side):
            if len(str(puzzle[i][j])) == 1:
                if j != side - 1:
                    if j % n == 0:
                        temp += '||  ' + str(puzzle[i][j]) + '  |  '
                    elif j % n == n - 1:
                        temp += str(puzzle[i][j]) + '  '
                    else:
                        temp += str(puzzle[i][j]) + '  |  '
                else:
                    temp += str(puzzle[i][j]) + '  ||'
            else:
                if j != side - 1:
                    if j % n == 0:
                        temp += '|| ' + str(puzzle[i][j]) + '  |  '
                    elif j % n == n - 1:
                        temp += str(puzzle[i][j]) + ' '
                    else:
                        temp += str(puzzle[i][j]) + ' |  '
                else:
                    temp += str(puzzle[i][j]) + ' ||'
                
        print(temp)
        
        if i % n == n - 1:
            line = '-' * factor
            print(line)
    
    return

print("The grid:")
grid = generate_sudoku(4, verbose=True)

print("\n The puzzle:")
puzzle = generate_puzzle(grid, 100, verbose=True)

print("The Solution:")
solution = annealer.solve_sudoku_by_blocks(puzzle)
if validate_sudoku(solution):
    print_grid(solution)
else:
    print("Did not solve. This is a random solver, so expect a different outcome every time. Try again!")
