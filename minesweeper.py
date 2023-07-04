
# create minesweeper grid function
def minesweeper_grid(rows, columns):
   
    grid = [['#', '-', '-', '#', '-'], 
            ['-', '-', '#', '-', '-'],
            ['#', '-', '-', '#', '#'], 
            ['-', '#', '#', '-', '-'],
            ['#', '-', '-', '#', '-']]
    
    # Print the initial grid
    print("Initial Minesweeper Grid:")
    print_minesweeper_grid(grid)

    # Fill in numbers indicating the number of surrounding mines and use the count 
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] != '#':
                count = 0
                
                # Check surrounding cells for mines by giving the parameters in which to search using indexing min and max
                for r in range(max(0, row - 1), min(rows, row + 2)):
                    for c in range(max(0, col - 1), min(columns, col + 2)):
                        if grid[r][c] == '#':
                            count += 1
                if count > 0:
                    grid[row][col] = str(count)
    
    return grid

# Function to print the Minesweeper grid and adding a space between elements for readability
def print_minesweeper_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

#ensure that the for loop code iterates across all rows and columns to print
rows = 5
columns = 5

minesweeper = minesweeper_grid(rows, columns)
print("Minesweeper Grid:")
print_minesweeper_grid(minesweeper)



