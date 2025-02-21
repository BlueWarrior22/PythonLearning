import random
import string


len_list_parameter = random.randint(1,9)

def shuffle_list():
    list_parameter = []
    for i in range(len_list_parameter):
        list_item = ''.join(random.choices(string.ascii_letters + string.digits, k=len_list_parameter))
        list_parameter.append(list_item)
    print(list_parameter)    
    random.shuffle(list_parameter)
    return list_parameter

print(shuffle_list())