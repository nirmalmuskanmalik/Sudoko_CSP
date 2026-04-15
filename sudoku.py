# Sudoku CSP Solver using Backtracking with constraint propagation

from collections import deque

rows = "ABCDEFGHI"
cols = "123456789"

def cross(A, B):
    return [a + b for a in A for b in B]

cells = cross(rows, cols)

# Create domains
def create_domains(grid):
    domains = {}
    for i, cell in enumerate(cells):
        if grid[i] == '0':
            domains[cell] = set('123456789')
        else:
            domains[cell] = set(grid[i])
    return domains

# Units
row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
box_units = [cross(rs, cs) for rs in ("ABC","DEF","GHI") for cs in ("123","456","789")]
units = row_units + col_units + box_units

# Neighbors
neighbors = {cell: set() for cell in cells}
for unit in units:
    for cell in unit:
        neighbors[cell].update(set(unit) - {cell})

# Constraint propagation
def propagate(domains):
    """Propagate constraints and return False if contradiction"""
    changed = True
    while changed:
        changed = False
        
        # Naked singles: if cell has one value, remove it from peers
        for cell in cells:
            if len(domains[cell]) == 1:
                val = list(domains[cell])[0]
                for peer in neighbors[cell]:
                    if val in domains[peer]:
                        domains[peer].discard(val)
                        changed = True
                        if len(domains[peer]) == 0:
                            return False
        
        # Hidden singles: if value can only go in one place in a unit, assign it
        for unit in units:
            for digit in '123456789':
                places = [c for c in unit if digit in domains[c]]
                if len(places) == 0:
                    return False
                if len(places) == 1:
                    if len(domains[places[0]]) > 1:
                        domains[places[0]] = {digit}
                        changed = True
    
    return True

# Global counters
backtrack_calls = 0
failures = 0

# Select variable with minimum remaining values
def select_unassigned_variable(domains):
    unassigned = [(cell, len(domains[cell])) for cell in cells if len(domains[cell]) > 1]
    if not unassigned:
        return None
    return min(unassigned, key=lambda x: x[1])[0]

# Main backtracking solver
def backtrack(domains):
    global backtrack_calls, failures
    backtrack_calls += 1

    # Check if all cells are assigned
    if all(len(domains[cell]) == 1 for cell in cells):
        return domains

    # Propagate constraints
    if not propagate(domains):
        failures += 1
        return None

    cell = select_unassigned_variable(domains)
    if cell is None:
        return domains

    for value in list(domains[cell]):
        # Try assigning value to cell
        new_domains = {c: domains[c].copy() for c in cells}
        new_domains[cell] = {value}
        
        result = backtrack(new_domains)
        if result:
            return result

    failures += 1
    return None

# Print Sudoku nicely
def print_sudoku(domains):
    for r in rows:
        line = ""
        for c in cols:
            val = list(domains[r+c])[0]
            line += val + " "
            if c in "36":
                line += "| "
        print(line)
        if r in "CF":
            print("-" * 21)

# Solve function
def solve_sudoku(filename):
    global backtrack_calls, failures

    try:
        with open(filename, 'r', encoding='utf-8-sig') as f:
            grid = ''.join(f.read().split())
        
        if len(grid) != 81:
            print(f"Invalid grid size for {filename}: expected 81 chars, got {len(grid)}. Skipping...")
            return
    except FileNotFoundError:
        print(f"File {filename} not found. Skipping...")
        return

    backtrack_calls = 0
    failures = 0

    domains = create_domains(grid)

    result = backtrack(domains)

    if result:
        print(f"\nSolution for {filename}:")
        print_sudoku(result)
        print("Backtrack Calls:", backtrack_calls)
        print("Failures:", failures)
    else:
        print(f"No solution found for {filename}.")

# MAIN
if __name__ == "__main__":
    files = ["easy.txt", "medium.txt", "hard.txt"]

    for file in files:
        solve_sudoku(file)