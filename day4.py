from functools import reduce


input = open("day4.txt", "r").readlines()

def line_to_value(x,s):
    s = s.strip('\n').split(':')[1].split('|')
    s1 = set(s[0].split(' '))
    s2 = set(s[1].split(' '))
    s1.remove('')
    s2.remove('')

    res = len(s1 & s2)
    if res == 0: return x
    return x + 2**(len(s1 & s2)-1)


print(reduce(line_to_value, input,0))