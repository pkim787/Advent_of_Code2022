def listy_parser(listy):
    newlisty = []
    county = 0
    for element in listy:
        if element != "":
            newlisty.append(element)
        else:
            county +=1
            if county == 4: 
                newlisty.append("")
                county = 0
    return newlisty

def filey_reader(input_filey,output_filey):
    input_file = open(input_filey, 'r')
    output_file = open(output_filey, 'w')
    taby = []
    for line in input_file:
        if "[" in line:
            newline = line.rstrip("\n")
            listy = newline.split(" ")
            newlisty = listy_parser(listy)
            taby.append(newlisty)
        else: 
            if "move" in line:
                output_file.write(line)
    input_file.close()
    output_file.close()
    return taby

def stack_convert(taby):
    holder = []
    stacklist = []
    lentaby = len(taby)
    lenline = len(taby[1])
    for i in range(lenline):
        for x in range(lentaby):
            if taby[x][i] != '':
                holder.append(taby[x][i])
        holder.reverse()
        stacklist.append(holder)
        holder = []
    return stacklist

def filter_num(element):
    return True if element.isnumeric() else False

def parse_movements(input_file, output_file):
    replacefile = open(input_file, 'r')
    movementfile = open(output_file, 'w')
    for line in replacefile:
        elements = line.strip()
        elements = elements.split(" ")
        result = list(filter(filter_num, elements))
        result = ','.join(result)
        result += '\n'
        movementfile.write(result)
    replacefile.close()
    movementfile.close()

def move_stacks(stacklisty, movementfiley):
    movementfile = open(movementfiley, 'r')
    for line in movementfile:
        newline = line.strip()
        listy = newline.split(',')
        newlisty = [eval(i) for i in listy]
        #print(newlisty)
        for i in range(newlisty[0]):
            element = stacklisty[newlisty[1] - 1].pop()
            stacklisty[newlisty[2] - 1].append(element)
    return stacklisty
taby = filey_reader("SupplyInput.txt","ReplaceFile.txt")

stacklist = stack_convert(taby)

parse_movements("ReplaceFile.txt", "MovementFile.txt")

stacklist = move_stacks(stacklist, "MovementFile.txt")
newstr = ""
for elements in stacklist:
    letter = elements.pop()
    newstr += letter[1]

print(newstr)