input  = open("day6.txt", "r").readlines()

times = [int(i) for i in input[0].split(':')[1].split(' ') if i != '']
distances = [int(i) for i in input[1].split(':')[1].split(' ') if i != '']

ans = [0]*len(distances)

print(times)
print(distances)
for i,time in enumerate(times):
    for x in range(time):
        if  x*(time-x) > distances[i]: ans[i]+=1
        

print(ans)

res = 0
print(res)