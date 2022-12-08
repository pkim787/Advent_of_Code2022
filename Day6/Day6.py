# O(n^2) time complexity
def filey_reader(input_filey):
    input_file = open(input_filey, 'r')
    liney = input_file.readline()
    lengthy = len(liney)
    result = ""
    for indy in range(lengthy):
        holder = set()
        for j in range (indy, lengthy):
            if liney[j] in holder:
                # print(result)
                result = ""
                break
            else:
                holder.add(liney[j])
                result += liney[j]
                if len(result) == 14:
                    # print(result)
                    return j + 1

print(filey_reader("PacketStream.txt"))