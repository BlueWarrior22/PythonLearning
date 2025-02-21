'''Write a function that generates a six-digit/character randon_user_id'''

from random import random as r, randint
import string

def randon_user_id():
    user_id_str = str()
    for i in range(6):
        user_id_str += str(randint(0,9))
    return user_id_str

print(randon_user_id())


def genuserid ():
    useridramdon = str()
    for i in range (6):
        useridramdon += str(randint(0,9))
    return str(useridramdon)

print(genuserid())


import random
import string

#Select 2 digits at random:

def randonuserid ():

    digits = random.choices(string.digits, k=10)
    letter = random.choices(string.ascii_letters, k=10)
    randonuseridresult = ''.join(random.sample(digits+letter, 6))
    return randonuseridresult

print(randonuserid())

def user_id_gen_by_user():
    nchar = int(input('Number the characters: '))
    nids = int(input('Number of IDs: '))
    for i in range (nids):
        print(''.join(random.choice(string.ascii_letters+string.digits) for i in range(nchar)))

user_id_gen_by_user()

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    print(f'rgb ({red}, {green}, {blue})')

rgb_color_gen()