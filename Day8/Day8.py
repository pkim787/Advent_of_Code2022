def create_grid(input_file):
    filey = open(input_file, 'r')
    gridy = []
    for line in filey:
        liney = [int(tree) for tree in line.strip()]
        gridy.append(liney)
    return gridy

gridy = create_grid("TreeInput.txt")

def detect_visy(col, row, valy, gridy): 
    north_view = True
    south_view = True
    west_view = True
    east_view = True
    for north in range(col - 1, -1, -1):
        if gridy[north][row] >= valy:
            north_view = False
            break
    for south in range(col + 1, len(gridy)):
        if gridy[south][row] >= valy:
            south_view = False
            break
    for west in range(row - 1, -1, -1):
        if gridy[col][west] >= valy:
            west_view = False
            break
    for east in range(row + 1, len(gridy[0])):
        if gridy[col][east] >= valy:
            east_view = False
    
    if north_view == True or south_view == True or west_view == True or east_view: 
        return True
    else:
        return False
    

def parse_grid(gridy):
    cols = len(gridy)
    rows = len(gridy[0])
    counter = 0
    for i in range(0, cols):
        for j in range(0, rows):
            if i != 0 and j != 0 and i != (cols - 1) and j != (rows - 1):
                valy = gridy[i][j]
                bool = detect_visy(i, j, valy, gridy)
                if bool == True: 
                    counter += 1
            else: 
                counter += 1
    return counter
            
total = parse_grid(gridy)
print(total)

