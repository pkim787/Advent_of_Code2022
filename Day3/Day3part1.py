import string

# set values to each letter 1-52
loweralph = list(string.ascii_lowercase)
upperalph = list(string.ascii_uppercase)
point_value = {}
valy=1
for letter in loweralph: 
    point_value.update({letter:valy})
    valy += 1 
for letter in upperalph:
    point_value.update({letter:valy})
    valy += 1

#print(point_value)

#newy = 'fzmmmfwDWFzlQQqjCQjDGnqq'

# find duplicate characters in each compartment of a rucksack
def find_dupes(mystring):
    #print(mystring)
    string1 = mystring[:len(mystring)//2]
    #print(string1)
    string2 = mystring[len(mystring)//2:]
    #print(string2)
    letters = [*string1]
    dupes = set()
    for letter in letters:
        if letter in string2:
            dupes.add(letter)
    #print(dupes)
    return dupes


input_filey = open("RuckInput.txt", "rt")

totScore = 0

for line in input_filey:
    #print(line)
    newline = line.strip()
    holden = find_dupes(newline)
    #print(holden)
    for dupe in holden: 
        if dupe in point_value.keys():
            totScore += point_value.get(dupe)

input_filey.close()

print(totScore)
