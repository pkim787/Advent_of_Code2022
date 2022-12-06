input_filey = open("GameInput.txt", "rt")
output_filey = open("ReplaceFile.txt", "wt")

for line in input_filey:
    newline = (line.replace('A', "rock")) 
    newline = (newline.replace('B', "paper")) 
    newline = (newline.replace('C', "scissors"))
    newline = (newline.replace('X', "lose")) 
    newline = (newline.replace('Y', "draw")) 
    newline = (newline.replace('Z', "win"))
    #print(newline)
    output_filey.write(newline)
input_filey.close()
output_filey.close()

new_filey = open("ReplaceFile.txt", 'r')
score = 0
rock = 1
paper = 2
scissors = 3 

for line in new_filey:
    enemy,meme = line.split()
    if meme == "draw":
        if enemy == "rock":
            score += 4
        if enemy == "paper":
            score += 5
        if enemy == "scissors":
            score += 6
    if meme == "lose":
        if enemy == "rock":
            score += 3
        if enemy == "paper":
            score += 1
        if enemy == "scissors":
            score += 2
    if meme == "win":
        if enemy == "rock":
            score += 8
        if enemy == "paper":
            score += 9
        if enemy == "scissors":
            score += 7

new_filey.close() 

print(score)