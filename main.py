from ascii_art import tela

from ascii_art import full, empty
import random
text = ''.join([full, full, empty, full,full, full, empty, empty, full, full, empty])


def geradorDeGrid():
    grid = []
    for _ in range(10):  # Assuming a grid size of 10x10
        row = []
        for _ in range(20):
            cell = random.randint(0, 1)  # Generate a random integer between 0 and 1
            row.append(cell)
        grid.append(row)
    return grid

def construtorDeTela(grid):
    thisGrid = []
    for row in grid:
        thisRow = []
        for cell in row:
            if cell == 1:
                thisRow.append(full)
            else:
                thisRow.append(empty)
        thisGrid.append(thisRow)
    for line in thisGrid:
        print(''.join(line))
    print(grid)
        

print(construtorDeTela(geradorDeGrid()))

# grid = geradorDeGrid()

"""
print(text)
x = 0
for i in range(1, len(text), 2):
    if text[i] == '█':
        print( x, "= alive")
    else:
        print( x, "= dead")
    x = x + 1
"""
