input  = open("day6.txt", "r").readlines()

times = [int(input[0].split(':')[1].replace(' ','').replace('\n','') )]
distances = [int( input[1].split(':')[1].replace(' ','').replace('\n',''))]

ans = [0]*len(distances)

print(times)
print(distances)
for i,time in enumerate(times):
    for x in range(time):
        if  x*(time-x) > distances[i]: ans[i]+=1
        

print(ans)

res = 0
print(res)