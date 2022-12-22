from importlib.util import set_loader
from pickle import TRUE
from random import choice

class Nucleotide:
    def __init__(self, _str):
        self.str = _str

    @classmethod
    def list_to_str(cls, _lst):
        return cls("".join(_lst))

    def __mul__(self, sec_num):
        if len(self.str) < len(sec_num.str):
            min_len = len(self.str)
        else:
            min_len = len(sec_num.str)

        new_str = []
        for elem in zip(self.str, sec_num.str):
            new_str.append(choice(elem))

        return self.list_to_str(new_str[:min_len])

    def __add__(self, sec_num):
        return self(self.str + sec_num.str)

    def __eq__(self, sec_num):
        if self.str == sec_num.str:
            return True
        else:
            return False

class RNA(Nucleotide):
    possible_elem = ['A', 'U', 'G', 'C']
    elem_transform = {
        'A': 'T',
        'U': 'A',
        'G': 'C',
        'C': 'G'
    }
    
    def __init__(self, _str):
        for elem in _str:
            if elem not in self.possible_elem:
                raise ValueError(f"Incorrect element - ({elem}) in {type(self).__name__}!")
        
        super().__init__(_str)

    def make_transform(self):
        return DNA.list_to_str([self.elem_transform[elem] for elem in self.str])

    def __getitem__(self, i):
        return self.str[i]

    def __str__(self):
        return self.str

    def __repr__(self):
        return f"{type(self).__name__} (str = {self.str})"
    
class DNA(RNA):
    possible_elem = ['A', 'T', 'G', 'C']
    elem_transform = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    def __init__(self, _str, _str_2 = None):
        super().__init__(_str)
        if _str_2 == None:
            self.sec_str = Nucleotide.list_to_str([self.elem_transform[elem] for elem in self.str]).str
        else:
            self.sec_str = _str_2

    def __getitem__(self, i):
        elem = super().__getitem__(i)
        sec_elem = self.elem_transform[elem]
        return elem, sec_elem

    def __str__(self):
        return f"({self.str}, {self.sec_str})"

    def __repr__(self):
        return f"{type(self).__name__} (str = {self.str}, sec_str = {self.sec_str})"
