import random
import string

def generate_colors(codi, numbers):
    if codi == 'hexa':
        hexa_color = []
        for i in range(numbers):
            hexa_random = '#'+''.join(random.choices(string.hexdigits, k=6))
            hexa_color.append(str(hexa_random))
        return(hexa_color)
    elif codi == 'rgb':
        rgb_color = []
        for i in range(numbers):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            rgb_random = 'rgb('+str(red)+', '+str(green)+', '+str(blue)+')'
            rgb_color.append(rgb_random)
        return(rgb_color)
    else:
        return('no color')

print(generate_colors('rgb', 3))