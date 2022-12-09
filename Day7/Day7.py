def filey_reader(input_file):
    filey = open(input_file, 'r')
    set_cmd = False
    dir_contents = []
    dir_stack = ["/"]
    full_dir = {}
    filey.readline()
    cur_dir = "/"
    ls_call = False
    for line in filey: 
        liney = line.strip()
        liney = liney.split()
        if liney[0] == "$":
            set_cmd = False
            if liney[1] == "cd":
                if ls_call:
                    full_dir.update({''.join(dir_stack): dir_contents})
                    dir_contents = []
                    ls_call = False
                # print(liney)
                if liney[2] != "..":
                    dir_stack.append(liney[2])
                    cur_dir = dir_stack[-1]
                else:
                    dir_stack.pop()
                    cur_dir = dir_stack[-1]
            if liney[1] == "ls":
                ls_call = True
                set_cmd = True
                continue
        if set_cmd == True:
            # print(liney)
            if liney[0].isnumeric(): 
                dir_contents.append(int(liney[0]))
            elif liney[0] == 'dir':
                newdir = ''.join(dir_stack) + liney[1]
                dir_contents.append(newdir)
    full_dir.update({''.join(dir_stack): dir_contents})            
    filey.clos()
    return full_dir

        

def sum_counter(dicty):
    tot = 0
    for key in dicty:
        if dicty[key] <= 100000:
            tot += dicty[key]
    return tot

def create_ref(dicty):
    ref_dicty = {}
    for keys, values in dicty.items():
        if len(values) == 1 and isinstance(values[0],int):
            ref_dicty.update({keys: values[0]})
    return ref_dicty

def total_counter(dicty):
    all_keys = dicty.keys() 
    ref_dicty = create_ref(dicty)
    while len(ref_dicty) != len(dicty):
        for mykeys in all_keys:
            # print(mykeys)
            ref_dicty = create_ref(dicty)
            tot = 0 
            update_listy = []
            for elem in dicty[mykeys]:
                # print(elem)
                if isinstance(elem, int):
                    tot += int(elem)
                else:
                    if elem in ref_dicty.keys():
                        tot += ref_dicty[elem]
                    else:
                        update_listy.append(elem)
            if tot != 0:
                update_listy.append(tot)
            dicty.update({mykeys: update_listy})
    

    return ref_dicty
    
def remove_smallest(ref_dicty):
    storey = ref_dicty['/']
    unused_space = 70000000 - storey
    min = 70000000
    min_key = ""
    for key, value in ref_dicty.items():
        new_value = unused_space + value
        if new_value >= 30000000 and new_value < min:
            min = new_value
            min_key = key
    return min_key 

full_tree = filey_reader("directoryinput.txt")

# ref_dicty = create_ref(full_tree)

# for key, value in full_tree.items():
#     print(key, " : ", value)

ref_dicty = total_counter(full_tree)

# for key, value in ref_dicty.items():
#     print(key, " : ", value)

new_key = remove_smallest(ref_dicty)

print(ref_dicty[new_key])
# print(sum_counter(ref_dicty))

