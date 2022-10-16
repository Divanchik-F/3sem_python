from random import randint

class Vector:
    def __init__(self, _x, _y, _z):
        self.x=float(_x)
        self.y=float(_y)
        self.z=float(_z)

    def __str__(self):
        return(f"({self.x}, {self.y}, {self.z})")

    def __add__(self, sec_num):
        return(Vector(self.x + sec_num.x, self.y + sec_num.y, self.z + sec_num.z))

    def __sub__(self, sec_num):
        return(Vector(self.x - sec_num.x, self.y - sec_num.y, self.z - sec_num.z))

    def __mul__(self, sec_num):
        return(self.x*sec_num.x+self.y*sec_num.y+self.z*sec_num.z)

    def __matmul__(self, sec_num):
        new_x=self.y*sec_num.z-self.z*sec_num.y
        new_y=self.z*sec_num.x-self.x*sec_num.z
        new_z=self.x*sec_num.y -self.y*sec_num.x
        return Vector(new_x, new_y, new_z)

    def __abs__(self):
        return((self.x**2+self.y**2+self.z**2)**0.5)

    @classmethod
    def str_constr(self, vec_str):
        return(Vector(*vec_str.split(',')))

    def __gt__(self, sec_num):
        if(abs(self)>abs(sec_num)):
            return True
        else:
            return False

    def __truediv__(self, num):
        return(Vector(self.x/num, self.y/num, self.z/num))

def task_2_3():
    N = int(input())
    mass_center=Vector(0, 0, 0)
    furthest_vec=Vector(0, 0, 0)
    for i in range(N):
        str=input()
        new_vec=Vector.str_constr(str)
        if(new_vec>furthest_vec):
            furthest_vec=new_vec
        mass_center=mass_center+new_vec
    mass_center=mass_center/N
    print(f"Mass center: {mass_center}, furthest vector: {furthest_vec}!")

def task_4():
    vec_1=Vector(1, 0, 0)
    vec_2=Vector(0, 1, 0)
    print(abs(vec_1@vec_2))

def task_5():
    vec_1=Vector(2, 0, 0)
    vec_2=Vector(0, 1, 0)
    vec_3=Vector(0, 0, 1)
    print(abs(vec_1*(vec_2@vec_3)))

def count_perim(vec_1, vec_2,  vec_3):
    perim=0
    perim+=abs(vec_1-vec_2)
    perim+=abs(vec_2-vec_3)
    perim+=abs(vec_3-vec_1)
    return perim

def count_s(vec_1, vec_2,  vec_3):
    val_1=(vec_2.x-vec_1.x)*(vec_3.y-vec_1.y)
    val_2=(vec_3.x-vec_1.x)*(vec_2.y-vec_1.y)
    return 0.5*abs(val_1-val_2)

def task_6_7():
    vec_list=[]
    perim=0
    s=0
    for i in range(20):
        vec_list.append(Vector(randint(-10, 10), randint(-10, 10), randint(-10, 10)))
    for i in range(20):
        for j in range(20):
            for k in range(20):
                new_perim=count_perim(vec_list[i], vec_list[j], vec_list[k])
                if new_perim>perim:
                    perim=new_perim
                new_s=count_s(vec_list[i], vec_list[j], vec_list[k])
                if new_s>s:
                    s=new_s
    
    print(f"Max perimeter: {perim}, max square area: {s}!")

task_2_3()
task_4()
task_5()
task_6_7()