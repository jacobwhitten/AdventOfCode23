from functools import reduce
input = open("day1.txt","r").readlines()

def first_last_number(s):
    result = ""
    for c in s:
        if c.isnumeric():
            result = c
            break
    for c in reversed(s):
        if c.isnumeric():
            result = result + c
            break

    return int(result)
def words_to_numbers(s:str):
    res = s.replace('one','o1one').replace('two','t2two').replace('three','t3three').replace('four','f4four').replace('five','f5five').replace('six','s6six').replace('seven','s7seven').replace('eight','e8eight').replace('nine','n9nine')
    return res

value = reduce(lambda x,y: x+y, map( first_last_number, map(words_to_numbers,input)))

print(value)