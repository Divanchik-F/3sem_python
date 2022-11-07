import os
import string

class TextLoader:
    def __init__(self, file_path):
        self.path = file_path
        self.files = os.listdir(self.path)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, i):
        file_name = f"{self.path}\{self.files[i]}"
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read().lower().translate(str.maketrans('', '', string.punctuation))
        
    def __iter__(self):
        for i in range(len(self.files)):
            yield self.__getitem__(i)

txt_loader = TextLoader("D:\ILab\Akkinator\Lesson 9\sample")
print(len(txt_loader))
print(txt_loader[0])
for i in txt_loader:
    print("\n\nNEXT TEXT\n\n")
    print(i)