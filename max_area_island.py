def max_area_of_island(grid):
    if not grid:
        return 0
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    max_area = 0
    def dfs(row, col, grid):
        area = 1
        grid[row][col] = 0
        for direction in dirs:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[row]) and (
                grid[new_row][new_col] == 1):
                area += dfs(new_row, new_col, grid)
        return area
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                temp = dfs(row, col, grid)
                max_area = max(max_area, temp)
    return max_area
    
if __name__ == '__main__':
    # grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    #          [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #          [0,1,1,0,1,0,0,0,0,0,0,0,0],
    #          [0,1,0,0,1,1,0,0,1,0,1,0,0],
    #          [0,1,0,0,1,1,0,0,1,1,1,0,0],
    #          [0,0,0,0,0,0,0,0,0,0,1,0,0],
    #          [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #          [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid = [[0,0,0,0,0,0,0,0]]
    print(max_area_of_island(grid))