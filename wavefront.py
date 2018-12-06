X_SIZE = 5 #number of columns
Y_SIZE = 4 #number of rows

grid_map = [[0,0,2,0,0],
            [0,0,1,1,0],
            [0,0,1,0,0],
            [0,1,0,0,0]]
'''
grid_map = [[2,3,4,5,6],
            [3,4,1,1,7],
            [4,5,1,9,8],
            [5,1,11,10,9]]
'''
OBSTACLE = 1
GOAL = 2

def generate_neighouring_cells(current_cell):
    cells = []
    cur_row = current_cell[0]
    cur_col = current_cell[1]

    #UP CELL
    if cur_row - 1 >= 0:
        #cur_row = cur_row - 1
        cells.append((cur_row-1, cur_col, grid_map[cur_row-1][cur_col], 'up'))
        #cells.append((cur_col, cur_row-1, grid_map[cur_col][cur_row-1], 'up'))

    #DOWN CELL
    if cur_row + 1 < Y_SIZE:
        #cur_row = cur_row + 1
        cells.append((cur_row+1,cur_col, grid_map[cur_row+1][cur_col], 'down'))
        #cells.append((cur_col, cur_row+1, grid_map[cur_col][cur_row+1], 'down'))

    #RIGHT CELL
    if cur_col + 1 < X_SIZE:
        #cur_col = cur_col + 1
        cells.append((cur_row, cur_col+1, grid_map[cur_row][cur_col+1], 'right'))
        #cells.append((cur_col+1, cur_row, grid_map[cur_col+1][cur_row], 'right'))

    #LEFT CELL
    if cur_col - 1 >= 0:
        #cur_col = cur_col - 1
        cells.append((cur_row, cur_col-1, grid_map[cur_row][cur_col-1], 'left'))
        #cells.append((cur_col-1, cur_row,grid_map[cur_col-1][cur_row], 'left'))

    return cells

# Wavefront algorithm

def wave_front(start, world):
    queue = [start]

    while len(queue) != 0:
        cell = queue.pop(0)
        neighbours = generate_neighouring_cells(cell)

        for neighbour in neighbours:
            if grid_map[neighbour[0]][neighbour[1]] == 0:
                    
                grid_map[neighbour[0]][neighbour[1]] = grid_map[cell[0]][cell[1]] + 1
                queue.append(neighbour)


#print(generate_neighouring_cells((0,1)))
wave_front((0, 2), grid_map)
print(grid_map)
