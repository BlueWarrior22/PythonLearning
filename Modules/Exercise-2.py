'''
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
(six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 
0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

'''

import random
import string

def list_of_hexa_colors ():
    hexa_color = ["#"+"".join(random.choices(string.hexdigits, k=6))]
    return print(hexa_color)

list_of_hexa_colors()