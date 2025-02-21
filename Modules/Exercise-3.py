import random

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb_color = ['rgb ('+str(red)+', '+str(green)+', '+str(blue)+')']
    return print(rgb_color)

rgb_color_gen()