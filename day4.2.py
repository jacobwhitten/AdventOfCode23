from functools import reduce


input = open("day4.txt", "r").readlines()

counts = [1] * len(input)

def line_to_value(s):
    s = s.strip('\n').split(':')[1].split('|')
    s1 = set(s[0].split(' '))
    s2 = set(s[1].split(' '))
    s1.remove('')
    s2.remove('')
    return (len(s1 & s2))

for i,line in enumerate(input):
    #print(counts[i])
    #print(line_to_value(line))    
    for x in range(line_to_value(line)):
        counts[x+i+1]+= counts[i]


print(sum(counts))


