input  = open("day5.txt", "r").readlines()

input = list(filter(lambda s: s!='\n', input))



working_dict = [int(i) for i in input[0].split(' ')[1:]]
next_dict = []
state = [0]*len(working_dict)


for line in input[1:]:   
    if(not line[0].isnumeric()):
        working_dict = working_dict + next_dict
        state = [0]* len(working_dict)
        next_dict=[]
        continue
    arr = line.split(' ')
    dest = int(arr[0])
    source = int(arr[1])
    length = int(arr[2])
    i = 0
    while i < len(working_dict):
        seed= working_dict[i]
        seed_l = working_dict[i+1]
        if(seed< source):
            if(seed+seed_l> source+length):
                #seed starts before source and ends after source
                next_dict.append(dest)
                next_dict.append(length)
                working_dict.append(seed)
                working_dict.append(source-seed)
                working_dict.append(source+length)
                working_dict.append(seed+seed_l-(source+length))
                state.append(0)
                state.append(0)
                state.append(0)
                state.append(0)
                state[i] = 1
                state[i+1] = 1
            elif(seed+seed_l>source):
                #seed starts before source and ends before source+length
                next_dict.append(dest)
                next_dict.append(seed_l-(source-seed))
                working_dict.append(seed)
                working_dict.append(source-seed)
                state.append(0)
                state.append(0)
                state[i] = 1
                state[i+1] = 1
        elif(seed>=source and seed <source+length):
            if(seed+seed_l> source+length):
                #seed starts after source and ends after source
                next_dict.append((seed-source)+dest)
                next_dict.append((source+length)-seed)
                working_dict.append(source+length)
                working_dict.append(seed_l-((source+length)-seed))
                state.append(0)
                state.append(0)
                state[i] = 1
                state[i+1] = 1

            else:
                #seed starts after source but ends before source
                next_dict.append((seed-source)+dest)
                next_dict.append(seed_l)
                state[i] = 1
                state[i+1] = 1
        i+=2
    
    count= 0
    for i,x in enumerate(state):
        if x == 1: 
            working_dict.pop(i-count)
            count+=1
    state = [0]*len(working_dict)

working_dict = working_dict + next_dict
result = 9999999999999999999
for i,val in enumerate(working_dict):
    if (i%2)==0:
        result = min(result,val)
print(result)