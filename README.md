# Sudoku Solver Implementations

This repository contains implementations of Sudoku solvers in Python using different algorithms.

## Overview

Sudoku is a logic-based combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contain all of the digits from 1 to 9.

This repository provides four different implementations to solve Sudoku puzzles:

1. **Backtracking Algorithm**: Uses a recursive backtracking algorithm to solve Sudoku puzzles.

2. **Simulated Annealing Algorithm**: Uses simulated annealing, a probabilistic optimization algorithm, to solve Sudoku puzzles.

3. **Constraint Satisfaction Problem (CSP) Algorithm**: Implements a CSP solver to solve Sudoku puzzles.

4. **Rule-Based Algorithm**: Utilizes rule-based methods to solve Sudoku puzzles.

### Input Format

The input Sudoku puzzle should be provided as a 9x9 grid, where empty cells are represented by `0`.

Example input:

```
0 0 0 2 6 0 7 0 1
6 8 0 0 7 0 0 9 0
1 9 0 0 0 4 5 0 0
8 2 0 1 0 0 0 4 0
0 0 4 6 0 2 9 0 0
0 5 0 0 0 3 0 2 8
0 0 9 3 0 0 0 7 4
0 4 0 0 5 0 0 3 6
7 0 3 0 1 8 0 0 0
```

### Output

The solver will print the solved Sudoku puzzle or indicate if no solution exists.

## Contributors

PardeevReddy

---
