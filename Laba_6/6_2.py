class custom_float: #класс с дробным числом

    def __truediv__(self, sec_num): #оператор деления
        num1 = self.bin_to_float()
        num2 = sec_num.bin_to_float()
        res_num = custom_float(self.bit_len, self.mantiss_len, num1 / num2)
        return res_num

    def __add__(self, sec_num): #оператор сложения
        num1 = self.bin_to_float()
        num2 = sec_num.bin_to_float()
        res_num = custom_float(self.bit_len, self.mantiss_len, num1 + num2)
        return res_num

    def __sub__(self, sec_num): #класс вычитания
        num1 = self.bin_to_float()
        num2 = sec_num.bin_to_float()
        res_num = custom_float(self.bit_len, self.mantiss_len, num1 - num2)
        return res_num
    
    def __mul__(self, sec_num): #класс умножения
        num1 = self.bin_to_float()
        num2 = sec_num.bin_to_float()
        res_num = custom_float(self.bit_len, self.mantiss_len, num1 * num2)
        return res_num

    def __init__(self, _bit_len, _mantiss_len, _num): #конструктор создающий число
        self.num = []
        if _bit_len <= _mantiss_len:
            print("Number length in bits can't be less or equal mantiss length!")
            exit()
        self.exp_len = _bit_len - _mantiss_len - 1 
        self.mantiss_len = _mantiss_len + 1
        self.exp_val = 127
        self.UFL = False
        self.OFL = False

        self.int_to_bin(_num) #переводим целую часть в двоичный вид
        #print(self.num)

        self.float_part_to_bin(abs(_num - int(_num)), int(_num))#переводим дробную часть в двоичный вид
        #print(self.num)

        if self.exp_val < 104:
            self.UFL = True
        elif self.exp_val > 256:
            self.OFL = True
        else:
            exp_bin = format(self.exp_val, 'b')
            for i in range(0, self.exp_len - len(exp_bin)):
                self.num.append(0)
                print(0, end = '')
            for i in range(self.exp_len - len(exp_bin), self.exp_len):
                self.num.append(int(exp_bin[i - self.exp_len + len(exp_bin)]) - int('0'))
                #print(exp_bin[i - self.exp_len + len(exp_bin)], end = '')
            print()
        print(self.num, len(self.num))


    def int_to_bin(self, num): #Перевод числа из двоичного в десятичное
        abs_num = int(num)
        if num < 0:
            abs_num = abs(int(num)) #Получение модуля нужного числа
    
        bin_num = format(abs_num, 'b') #Перевод модуля числа в его двоичное представление

        if len(bin_num) >= self.mantiss_len: #Если двоичное представление числа больше разрядности ЭВМ, то здесь обрезаются его старшие биты
            bin_num = bin_num[::-1] 
            bin_num = bin_num[0:self.mantiss_len:1]
            bin_num = bin_num[::-1]
            for i in range(self.mantiss_len):
                self.num.append(int(bin_num[i]) - int('0')) #Превращаем строку в список для удобства

            for i in range(len(bin_num)):
                pass
                
        else: #Если двоичное число меньше разрядности ЭВМ, то здесь оно правильно запишется в память
            if num < 0: #Перевод для отрицательного числа
                self.num.append(1)
            else:
                self.num.append(0)

            if abs_num != 0:
                start = 0
                for i in range(len(bin_num)):
                    if bin_num[i] == '1':
                        start = i + 1
                        break
                for i in range(start, len(bin_num)):
                    self.num.append(int(bin_num[i]) - int('0'))
                    self.exp_val += 1

            print(self.num)

    def float_part_to_bin(self, num, int_num): #функция переводящая дробную часть в двочиный вид
        one_check = False
        if num == 0:
            for i in range(len(self.num) + 1, self.mantiss_len):
                self.num.append(0)
            self.exp_val = 127
        elif int_num == 0:
            one_check = False
            i = len(self.num)
            while i < self.mantiss_len:
                num *= 2
                if int(num) == 1:
                    if one_check:
                        self.num.append(1)
                        num -= 1
                        i += 1
                    else:
                        self.exp_val -= 1
                        num -= 1
                        one_check = True    
                elif one_check:
                    i += 1
                    self.num.append(0)
                else:
                    self.exp_val -= 1
        else:
            for i in range(len(self.num), self.mantiss_len):
                num *= 2
                if int(num) == 1:
                    self.num.append(1)
                    num -= 1   
                else:
                    self.num.append(0)
        
        print(self.num, self.exp_val, len(self.num))

    def bin_to_float(self): #функция переводящая двоичное число в дробное
        num = 0
        m = self.bit_len - self.mantiss_len

        temp = 1
        for i in range(1, m): #Перевод из двоичного в целую часть
            num += temp * self.num[m - i]
            temp *= 2
        temp = 1
        for i in range(m, self.bit_len): #Перевод из двоичного в дробную часть
            temp /= 2
            num += temp * self.num[i]
    
        if self.num[0] == 1: #Для отрицательных чисел            
            return float(-num) #Возвращаем значение, так как наше число отрицательное, пишем - перед ним

        else: #Случай если число положительное
            return float(num)  #Возвращаем итоговое значение

def check_epsilon(bit_len, mantiss_len): #Функция ищущее значение эпсилон
    check = custom_float(bit_len, mantiss_len, 1)
    two = custom_float(bit_len, mantiss_len, 2)
    while (True):
        old = check
        check = check / two
        if (old.bin_to_float() + check.bin_to_float() == old.bin_to_float()): #как только не можем различить разницу между двумя значениями заканчиваем цикл
            break

    print(f"Epsilon for {bit_len} bits len num, with {mantiss_len} bits mantiss len is: {old.bin_to_float()}")


def operand_test(num1, num2): #тесты операторов
    t1 = custom_float(32, 23, num1)
    t2 = custom_float(32, 23, num2)
    res1 = t1 + t2 #тест сложения
    if (res1.bin_to_float() == num1 + num2):
        print ("Operand addition test passed!")
    else: #кидаем исключение при ошибке
        raise NameError('Does not work for addition')

    res1 = t1 - t2 #тест вычитания
    if (res1.bin_to_float() == num1 - num2):
        print ("Operand subtraction test passed!")
    else: #кидаем исключение при ошибке
        raise NameError('Does not work for subtraction')

    res1 = t1 * t2 #тест умножения
    if (res1.bin_to_float() == num1 * num2):
        print ("Operand multiplication test passed!")
    else: #кидаем исключение при ошибке
        raise NameError('Does not work for multiplication')

    res1 = t1 / t2 #тест деления
    if (res1.bin_to_float() == num1 / num2):
        print ("Operand division test passed!\n")
    else: #кидаем исключение при ошибке
        raise NameError('Does not work for division')

t1 = custom_float(32, 23, 1234.323)