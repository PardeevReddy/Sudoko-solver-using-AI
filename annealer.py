import numpy as np
from random import sample, randint
import copy

TEMPERATURES = {'2': 0.5, '3': 0.5, '4': 0.5}

def solve_sudoku(puzzle_input, max_iterations=5000000, T=TEMPERATURES['3'], cooling_rate=1.0 - 1e-5, verbose=False):
    if verbose:
        print("Puzzle")

    reheat_rate = T / 0.3

    puzzle = copy.deepcopy(puzzle_input)
    side = len(puzzle)
    sq_size = int(np.sqrt(side))

    empty_cells = initialize(puzzle)

    if verbose:
        print("Initialized puzzle")

    score = calc_score(puzzle)
    target_score = -2 * side * side
    best_score = score
    stuck_count = 0

    for i in range(max_iterations):
        if i % 10000 == 0 and verbose:
            print("Iteration " + str(i) + ", current score:" + str(score) + "  Best score: " + str(best_score))

        if score == target_score or T == 0:
            break

        if stuck_count > 5000 or T < 1e-4:
            print("Annealer is stuck at T={} and stuck_count={}, so re-initializing...".format(T, stuck_count))
            T = T * reheat_rate
            puzzle = copy.deepcopy(puzzle_input)
            empty_cells = initialize(puzzle)
            stuck_count = 0

        neighbor_puzzle = find_neighbor(puzzle, empty_cells)
        s2 = calc_score(neighbor_puzzle)
        delta_s = float(score - s2)
        probability = np.exp(delta_s / T)

        random_probability = np.random.uniform(low=0, high=1, size=1)

        if probability > random_probability:
            puzzle = copy.deepcopy(neighbor_puzzle)
            score = s2
            if score < best_score:
                best_score = score
            stuck_count = 0

        stuck_count += 1

        T = cooling_rate * T

    if verbose:
        print("Total number of iterations done: ", i + 1, " to get score:", score)
        print("Solution:")

    return puzzle


def map_empty_cells(empty_cells, dim):
    empty_puzzle_cells = []

    for row in range(dim):
        for col in empty_cells[row]:
            empty_puzzle_cells.append((row + dim * (sqcount // dim), col + dim * (sqcount % dim)))
    return empty_puzzle_cells


def initialize(puzzle):
    side = len(puzzle)
    sq_size = int(np.sqrt(side))

    i = 0
    j = 0
    empty_cells = []
    square = []
    square_count = 0
    while i < side and j < side:

        square.append(puzzle[i][j:j + sq_size])

        if (i + 1) % sq_size == 0 and (j + sq_size) % sq_size == 0:

            fixed_cells = []
            empty = []

            values = list(range(1, side + 1))
            for row in range(sq_size):
                empty.append(np.where(np.array(square)[row] == 0)[0].tolist())
                fixed_cells.append(np.where(np.array(square)[row] != 0)[0].tolist())

                for f in fixed_cells[row]:
                    values.remove(square[row][f])

            index_map = map_empty_cells(empty, sq_size)
            empty_cells.append(index_map)

            for cell in index_map:
                random_val = sample(values, 1)[0]

                puzzle[cell[0]][cell[1]] = random_val

                values.remove(random_val)

            square_count += 1
            j += sq_size
            i -= sq_size
            square = []
            if j % side == 0:
                i = i + sq_size
                j = 0

        i += 1

    return empty_cells


def calc_score(puzzle):
    side = len(puzzle)
    score = 0

    puzzle_transpose = list(zip(*puzzle))
    for i in range(side):
        score -= len(list(set(puzzle[i])))
        score -= len(list(set(puzzle_transpose[i])))

    return score


def find_neighbor(puzzle, empty_cells):
    side = len(puzzle)
    sq_size = int(np.sqrt(side))
    new_puzzle = copy.deepcopy(puzzle)

    empty_block_size = 0
    while empty_block_size < 2:
        block = randint(0, side - 1)
        empty_block_size = len(empty_cells[block])

    a, b = sample(range(len(empty_cells[block])), 2)
    cell1, cell2 = empty_cells[block][a], empty_cells[block][b]

    new_puzzle[cell1[0]][cell1[1]], new_puzzle[cell2[0]][cell2[1]] = new_puzzle[cell2[0]][cell2[1]], new_puzzle[
        cell1[0]][cell1[1]]

    return new_puzzle