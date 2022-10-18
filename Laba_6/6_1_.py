class Complex:
    def __init__(self, _re, _im):
        self.re=_re
        self.im=_im
    
    def __add__(self, sec_num):
        return Complex(self.re+sec_num.re, self.im+sec_num.im)

    def __sub__(self, sec_num):
        return Complex(self.re-sec_num.re, self.im-sec_num.im)

    def __mul__(self, sec_num):
        new_re=self.re*sec_num.re-self.im*sec_num.im
        new_im=self.im*sec_num.re+self.re*sec_num.im
        return Complex(new_re, new_im)

    def __truediv__(self, sec_num):
        denom=sec_num.re**2+sec_num.im**2
        new_re=(self.re*sec_num.re+self.im*sec_num.im)/denom
        new_im=(self.im*sec_num.re-self.re*sec_num.im)/denom
        return Complex(new_re, new_im)

    def __abs__(self):
        return (self.re**2+self.im**2)**0.5

    def __str__(self):
        return (str(self.re)+' + '+str(self.im)+'i')

num = Complex(2, 3)
print(num)
