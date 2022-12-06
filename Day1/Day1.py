hiTot = 0
nextTot = 0
thirdTot = 0
temp = 0
ToT = 0
with open('calorieinput.txt') as calinput:
    lines = calinput.readlines()
    for line in lines:
        if line == "\n":
            if hiTot <= temp: 
                thirdTot = nextTot
                nextTot = hiTot
                hiTot = temp
                temp = 0
            elif hiTot > temp and nextTot <= temp: 
                thirdTot = nextTot
                nextTot = temp
                temp = 0
            elif hiTot > temp and nextTot > temp and thirdTot <= temp:
                thirdTot = temp
                temp = 0 
            else: 
                temp = 0
        else: 
            temp += int(line)

ToT = hiTot + nextTot + thirdTot
print(ToT)