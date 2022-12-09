def create_grid(input_file):
    filey = open(input_file, 'r')
    gridy = []
    for line in filey:
        liney = [int(tree) for tree in line.strip()]
        gridy.append(liney)
    return gridy

gridy = create_grid("TreeInput.txt")

def detect_visy(col, row, valy, gridy): 
    north_view = 0
    south_view = 0
    west_view = 0
    east_view = 0
    for north in range(col - 1, -1, -1):
        if gridy[north][row] < valy:
            north_view += 1
        if gridy[north][row] >= valy:
            break
    for south in range(col + 1, len(gridy)):
        if gridy[south][row] < valy:
            south_view += 1
        if gridy[south][row] >= valy:
            south_view += 1
            break
    for west in range(row - 1, -1, -1):
        if gridy[col][west] < valy: 
            west_view += 1
        elif gridy[col][west] >= valy:
            west_view += 1
            break
    for east in range(row + 1, len(gridy[0])):
        if gridy[col][east] < valy: 
            east_view += 1
        elif gridy[col][east] >= valy:
            east_view += 1
            break
    scenic_value = int(north_view) * int(south_view) * int(west_view) * int(east_view)
    return scenic_value
    

def parse_grid(gridy):
    cols = len(gridy)
    rows = len(gridy[0])
    scenic_value = 0
    for i in range(0, cols):
        for j in range(0, rows):
            if i != 0 and j != 0 and i != (cols - 1) and j != (rows - 1):
                valy = gridy[i][j]
                holder = detect_visy(i,j,valy,gridy)
                scenic_value = max(scenic_value, holder)
    return scenic_value
            
total = parse_grid(gridy)
print(total)



