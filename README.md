# Sudoko_CSP
# Sudoku Solver using Constraint Propagation & Backtracking

# Overview

This project is a **Sudoku Solver** implemented in Python. It solves Sudoku puzzles of different difficulty levels (easy, medium, hard) using:

* **Constraint Propagation**
* **Backtracking Search**
* **MRV (Minimum Remaining Values) Heuristic**

The program reads Sudoku puzzles from text files and prints the solved grid along with performance statistics.


# Objectives

* To solve Sudoku puzzles efficiently
* To apply AI techniques like constraint satisfaction
* To compare performance on different difficulty levels

# Working

# 1. Grid Representation

* Sudoku grid is represented as a string of **81 characters**
* `'0'` represents an empty cell
* Each cell is labeled (e.g., A1, B3, etc.)


# 2. Domains

* Each cell has a **domain** (possible values)
* If a cell is empty → domain = {1–9}
* If filled → domain = that single value


# 3. Constraints

The solver ensures:

* No repeated numbers in a **row**
* No repeated numbers in a **column**
* No repeated numbers in a **3×3 box**


# 4. Constraint Propagation

This step reduces possible values by:

* Removing assigned values from neighboring cells
* Assigning values when only one option is left

If a contradiction occurs (empty domain), it stops.

# 5. Backtracking Search

If the puzzle is not solved:

* Select a cell with **fewest possible values (MRV heuristic)**
* Try each value recursively
* Backtrack if a choice leads to failure


# Key Functions

* `create_domains()` → Initializes domains
* `propagate()` → Applies constraint propagation
* `backtrack()` → Solves using recursion
* `select_unassigned_variable()` → Chooses best cell (MRV)
* `print_sudoku()` → Displays solution
* `solve_sudoku()` → Main function for solving files

# Input Files

The program expects three files:

* `easy.txt`
* `medium.txt`
* `hard.txt`

Each file should contain:

* A Sudoku puzzle as a single line (81 digits)
* Use `0` for empty cells

# How to Run

1. Place input files in the same directory
2. Run the program:

python sudoku_solver.py

# Output

For each puzzle, the program prints:

* Solved Sudoku grid
* Number of **backtrack calls**
* Number of **failures**

# Example Output

Solution for easy.txt:
5 3 4 | 6 7 8 | 9 1 2
...
Backtrack Calls: 10
Failures: 2

# Features

* Efficient solving using AI techniques
* Works for different difficulty levels
* Tracks performance metrics
* Clean and readable output

---

# Limitations

* Input must be exactly **81 characters**
* Only supports standard 9×9 Sudoku
* Performance may slow for extremely complex puzzles

# Conclusion

This project demonstrates how **Constraint Satisfaction Problems (CSP)** can be solved using:

* Constraint propagation for efficiency
* Backtracking for completeness

It provides a strong foundation for understanding AI-based problem solving.

# Author
NIRMAL MUSKAN
