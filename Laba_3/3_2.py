import random
import string


def write_array(array, fifi):
    if len(array)>0:
        fifi.write(array[0])
        array.pop(0)
        write_array(array, fifi)
    return

    
array=[]
for i in range(1,8):
    letters = string.ascii_lowercase
    rand_string = str(i)+''.join(random.choice(letters) for i in range(i*2))+'\n'
    array.append(rand_string)

with open("fifi.txt", "w") as fifi:
    write_array(array, fifi)

