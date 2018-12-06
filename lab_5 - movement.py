import turtle
wn = turtle.Screen()

'''from ev3dev.ev3 import *
from movement.ev3movement.movement import *
btn = ev3.Button()'''

grid_map = [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 2, 0, 0]]
X_SIZE = 5 #number of columns
Y_SIZE = 4 #number of rows
OBSTACLE = 1
GOAL = 2
face = 1 #Represents the orientation of the robot (0 - facing up, 1- facing right, 2-facing down, 3-facing left)
move = 1 #Represents the direction the robot should move in (1 - move up, 2- move right, 3- move down, 4- move left)
cur_row1 = 2 #Start Row
cur_col1 = 1 #Start Column
start = (3,2)#Actually the goal - where wavefront starts planning from

ethel = turtle.Turtle()
ethel.left(90)
#________________________________________________________________________________
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
#___________________________________________________________________________________

#____________Wave Front___________
queue = [start]
while len(queue) != 0:
    cell = queue.pop(0)
    neighbours = generate_neighouring_cells(cell)

    for neighbour in neighbours:
        if grid_map[neighbour[0]][neighbour[1]] == 0:
                    
            grid_map[neighbour[0]][neighbour[1]] = grid_map[cell[0]][cell[1]] + 1
            queue.append(neighbour)

#__________________Create Plan_______________________________
current_pos = grid_map[cur_row1][cur_col1]
print(str(current_pos) + " at " + str(cur_row1) + " ," + str(cur_col1))
while current_pos != GOAL:
    try:
        #up = grid_map[cur_row - 1][cur_col] #correct value
        #right = grid_map[cur_row][cur_col + 1]#correct value
        #left = grid_map[cur_row][cur_col - 1]#correct value
        #down = grid_map[cur_row + 1][cur_col]#correct value
                    
        if ((cur_row1 -1 >= 0) and (grid_map[cur_row1 - 1][cur_col1] < current_pos) and (grid_map[cur_row1 - 1][cur_col1]!= OBSTACLE)):#checking cell at up position
            cur_row1 = cur_row1 - 1
            move = 1
            print("Move up")
        elif ((cur_col1 + 1 < X_SIZE) and (grid_map[cur_row1][cur_col1 + 1] < current_pos) and (grid_map[cur_row1][cur_col1 + 1] != OBSTACLE)):#checking cell at right position
            cur_col1 = cur_col1 + 1
            move = 2
            print("Move right")
        elif ((cur_row1 + 1 < Y_SIZE) and (grid_map[cur_row1 + 1][cur_col1] < current_pos) and (grid_map[cur_row1 + 1][cur_col1] != OBSTACLE)):#checking cell at down position
            cur_row1 = cur_row1 + 1
            move = 3
            print("Move Down")
        elif ((cur_col1 - 1 >= 0) and (grid_map[cur_row1][cur_col1 - 1] < current_pos) and (grid_map[cur_row1][cur_col1 - 1] != OBSTACLE)):#checking cell at left position
            cur_col1 = cur_col1 - 1
            move = 4
            print("move left")
        else:
            print("No decreasing path, shouldnt be possible...")
#__________________________________________________________________________________________________________
        

        current_pos = grid_map[cur_row1][cur_col1]

        ethel.right(((move - face)) * 90)#robot.turn_right_by_angel((move - face) * 90)
        ethel.forward(20)#robot.move_straight_line(48cm)
        face = move

        '''turn_right_by_angle((move - face) * 90, 450)
        move_straight_line(48, 450)#robot.move_straight_line(48cm)
        face = move'''
#_____________________________________________________________________________________________________________
        print(str(current_pos) + " at " + str(cur_row1) + " ," + str(cur_col1))
                
    except IndexError:
        continue

print("Done")


