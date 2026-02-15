# Create a function that takes a grid of # and -, where each hash represents a mine and each dash (-) represents an empty spot.

def minesweeper(grid):
    if not grid or not grid[0]:
        return grid
    
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    result = [row[:] for row in grid]  # Deep copy (good!)

    # Define the directions to check for neighboring mines
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '-':
                mines = sum(
                    1 for dr, dc in directions
                    if 0 <= (nr := r + dr) < rows and 0 <= (nc := c + dc) < cols and grid[nr][nc] == '#'
                )
                result[r][c] = str(mines)
    
    return result

# Define grid for testing:
input_grid = [
    ['-', '-', '-', '#', '#'],
    ['-', '#', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '#', '#', '-', '-'],
    ['-', '-', '-', '-', '-']
]       
output_grid = minesweeper(input_grid)
for row in output_grid:
    print(' '.join(row))                            