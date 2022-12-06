input_filey = open("GameInput.txt", "rt")
output_filey = open("ReplaceFile.txt", "wt")

for line in input_filey:
    newline = (line.replace('A', "rock")) 
    newline = (newline.replace('B', "paper")) 
    newline = (newline.replace('C', "scissors"))
    newline = (newline.replace('X', "rock")) 
    newline = (newline.replace('Y', "paper")) 
    newline = (newline.replace('Z', "scissors"))
    output_filey.write(newline)
input_filey.close()
output_filey.close()

new_filey = open("ReplaceFile.txt", 'r')
score = 0

for line in new_filey:
    enemy,meme = line.split()
    if enemy == "rock" and meme == "rock":
        score += 4 # using rock (1) + tie (3)
    if enemy == "rock" and meme == "paper":
        score += 8 # using paper (2) + win (6)
    if enemy == "rock" and meme == "scissors":
        score += 3 # using scissors (3) + lose (0)
    if enemy == "paper" and meme == "paper":
        score += 5 # using paper (2) + tie (3)
    if enemy == "paper" and meme == "scissors":
        score += 9  # using scissors (3) + win (6)
    if enemy == "paper" and meme == "rock":
        score += 1 # using rock (1) + lose (0)
    if enemy == "scissors" and meme == "scissors":
        score += 6 # using scissors (3) + tie (3)
    if enemy == "scissors" and meme == "rock":
        score += 7  # using rock (1) + win (6)
    if enemy == "scissors" and meme == "paper":
        score += 2 # using paper (2) + lose (0)

new_filey.close() 

print(score)