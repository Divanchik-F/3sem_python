import random
import string


with open("random_text.txt", "w") as file:
    for i in range(1,8):
        letters = string.ascii_lowercase
        rand_string = str(i)+''.join(random.choice(letters) for i in range(i*2))+'\n'
        #rand_string = str(i)
        file.write(rand_string)
    

with open("random_text.txt", "r") as file:
    for line in file:
        print(line.strip())

file.close()
