import string

def find_dupes(mystring1, mystring2, mystring3):
    letters = [*mystring1]
    dupes = set()
    holderset = set()
    for letter in letters:
        for letter2 in mystring2:
            if letter == letter2:
                holderset.add(letter)
        for letter3 in mystring3:
            for holder in holderset:
                if holder == letter3:
                    dupes.add(holder)
    return dupes

def badgefinder(line_group, point_value):
    if len(line_group) == 3:
            holden = find_dupes(line_group[0], line_group[1], line_group[2])
            for dupe in holden: 
                return point_value.get(dupe)

def file_reader(input_filey):
    line_group = []
    totScore = 0
    groups_of_lines = []

    # set values to each letter 1-52
    alph = list(string.ascii_lowercase)
    alph += list(string.ascii_uppercase)
    point_value = {}
    valy=1

    for letter in alph: 
        point_value.update({letter:valy})
        valy += 1 

    for line in input_filey:
        newline = line.strip()
        line_group.append(newline)
        if len(line_group) == 3:
            groups_of_lines.append(line_group)
            line_group =[]

    for groups in groups_of_lines:
        totScore += badgefinder(groups, point_value)
    input_filey.close()
    return totScore

filey = open("RuckInput.txt", "r")

print(file_reader(filey))

filey.close()
