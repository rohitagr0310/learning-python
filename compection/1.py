def checkSquare(grid, color):
    for i in range(2):
        for j in range(2):
            if grid[i][j] != color:
                return False
    return True


def canFormSquare(grid):
    for i in range(2):
        for j in range(2):
            color = grid[i][j]
            if checkSquare([row[j : j + 2] for row in grid[i : i + 2]], color):
                return True

    # Check if changing one cell can create a square
    for i in range(3):
        for j in range(3):
            temp = grid[i][j]
            grid[i][j] = "B" if temp == "W" else "W"
            for a in range(2):
                for b in range(2):
                    color = grid[a][b]
                    if checkSquare([row[b : b + 2] for row in grid[a : a + 2]], color):
                        return True
            grid[i][j] = temp

    return False


# Test cases
grid1 = [["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]
grid2 = [["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]
grid3 = [["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]

print(canFormSquare(grid1))  # Output: True
print(canFormSquare(grid2))  # Output: False
print(canFormSquare(grid3))  # Output: True
