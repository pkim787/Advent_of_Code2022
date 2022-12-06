def extend_range(mystring):
    listy = []
    a, b = mystring.split('-')
    a, b = int(a), int(b)
    listy.extend(range(a, b+1))
    return listy

def listy_compare(mylist1, mylist2):
    if len(mylist1) < len(mylist2):
        biglisty = mylist2
        smollisty = mylist1
        return biglisty, smollisty
    else:
        biglisty = mylist1
        smollisty = mylist2
        return biglisty, smollisty

def filey_reader(input_filey):
    allcounty = 0
    anycounty = 0
    for line in input_filey:
        party1, party2 = line.split(',')
        extendy1 = extend_range(party1)
        extendy2 = extend_range(party2)
        greatList, lessList = listy_compare(extendy1, extendy2)
        checky = all(item in greatList for item in lessList) # for part 1
        checky2 = any(item in greatList for item in lessList) # for part 2
        if checky:
            allcounty +=1
        if checky2:
            anycounty +=1
    return allcounty, anycounty

filey = open("CleanupInput.txt", "r")

print(filey_reader(filey))

filey.close()
