def numberOfRightTriangles(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Create dictionaries to store the counts of 1s in rows and columns
    row_counts = [0] * rows
    col_counts = [0] * cols

    # Count the number of 1s in each row and column
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                row_counts[i] += 1
                col_counts[j] += 1

    # Iterate through each cell and check for right triangles
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # For each cell with value 1, there can be right triangles
                # with other cells in the same row and same column
                count += (row_counts[i] - 1) * (col_counts[j] - 1)

    return count


# Test cases
grid1 = [[0, 1, 0], [0, 1, 1], [0, 1, 0]]
print(numberOfRightTriangles(grid1))  # Output: 2

grid2 = [[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
print(numberOfRightTriangles(grid2))  # Output: 0

grid3 = [[1, 0, 1], [1, 0, 0], [1, 0, 0]]
print(numberOfRightTriangles(grid3))  # Output: 2
