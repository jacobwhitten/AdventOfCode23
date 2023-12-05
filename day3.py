input = open("day3.txt", "r").readlines()

#print(input)

sum =0
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
                    found= (not ch.isnumeric() and not ch=="." and not ch=="\n")
                    #if found: print(ch)
                    include= include or (not ch.isnumeric() and not ch=="\n" and not ch==".") 
            if include:
                #print(num)
                sum+= int(num)
            num=""
            include = False



print(sum)
