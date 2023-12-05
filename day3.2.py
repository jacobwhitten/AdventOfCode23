input = open("day3.txt", "r").readlines()

#print(input)

sum =0
dicts = {}
for x,l in enumerate(input):
    num=""
    for y,ch in enumerate(l):
        #print(ch)
        #print(x)
        #print(y)
        if ch.isnumeric():
            num = num +ch
            #print(num)
        elif num != "":
            #check if nex tto symbol
            include=False
            for sy in range(max(0,x-1),min(len(input),x+2)):
                for sx in range(max(0,y-len(num)-1),min(len(input[sy]),y+1)):
                    line= input[sy]
                    #print(sx)
                    ch= line[sx]
                    if ch=="*":
                        key = ",".join([str(sy),str(sx)])
                        if key in dicts:
                            sum += dicts[key]*int(num)
                        else:
                            dicts[key] = int(num)
            num=""
            include = False



print(sum)