import shutil
import os


shutil.unpack_archive("main.zip")
Q=[]
for cd, dirs, files in os.walk("main"):
    for i in files:
        if i.endswith(".py"):
            if cd not in Q:
                Q.append(cd)
            break
Q=sorted(Q)
with open("3_3.txt", "w") as file:
    file.write("\n".join(Q))
