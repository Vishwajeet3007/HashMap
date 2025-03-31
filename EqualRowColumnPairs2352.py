def equalPairs(grid):
    
    n = len(grid)
    count = 0
    # using Brute force
    # for row in range(n):
    #     for col in range(n):
    #         is_equal = True
    #         for i in range(n):
    #             if grid[row][i] != grid[i][col]:
    #                 is_equal=  False
    #                 break
    #         if is_equal == True:
    #             count += 1

    # using hashmap
    mp = {}
    for row in grid:
        row_tuple = tuple(row)
        mp[row_tuple] = mp.get(row_tuple,0) + 1
    for col in range(n):
        temp = tuple(grid[row][col] for row in range(n))
        count += mp.get(temp,0)
    return count
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(equalPairs(grid))

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(equalPairs(grid))