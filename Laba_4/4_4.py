from time import time


def info(path):
    
    def dec(func):
        file=open(path, 'w', encoding='utf8')

        def dec2(*args, **kwargs):
            st_t=time()
            R=func(*args, **kwargs)
            e_t=time()
            file.write(str(st_t)+'\n')
            file.write(' '.join(list(map(str, args)))+' ')
            for k, v in kwargs.items():
                file.write(f"{k}={v} ")
            file.write('\n'+('-' if R is None else str(R))+'\n')
            file.write(str(e_t)+'\n')
            file.write(str(e_t-st_t)+'\n')
            file.close()
            return R
        
        return dec2

    return dec


@info("qwerty.txt")
def func(a1, a2, a3, a4, a5, a6, a7=None, a8=None):
    print(a1+a2-a3*a4+(a6/a5), a7, a8)

func (1, 2, 3, 4, 1, 2, a7=5, a8=4)
