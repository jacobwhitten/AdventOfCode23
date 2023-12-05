input  = open("day5.txt", "r").readlines()

input = list(filter(lambda s: s!='\n', input))

result = 999999999999999999
for seed in input[0].split(' ')[1:]:
    seed = int(seed)
    for line in input[1:]:   
        if(not line[0].isnumeric()):
            #restart looking
            # print("next map")
            # print(line)
            found = False
            continue
        arr = line.split(' ')
        dest = int(arr[0])
        source = int(arr[1])
        length = int(arr[2])
        if(not found and source<=seed<source+length):
            # print(seed)
            # print(arr)
            found = True
            seed = (seed-source) + dest

    result = min(result, seed)  


print(result)