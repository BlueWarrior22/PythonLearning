#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

import random as r
import string as s

def gen():
    return ''.join(r.choices(s.digits, k=1))

def randomArray ():
    items_array = set()
    while len(items_array) < 7:
        items_array.add(gen())
    return list(items_array)

print(randomArray())