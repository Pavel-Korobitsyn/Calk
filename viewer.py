import random

numb_type = 'r'
numb_value = 0
numb_oper = '+'
rd = random.randint(0,1)

def get_type(flag):
    global numb_type
    if flag == 0:
        chck = True
        while(chck): 
            chck = True
            numb_type = input('Выберете тип чисел (r - рациональные, c - комплексные): ')
            if numb_type in ('r','c'): chck = False
    elif flag == 1: numb_type = 'r'
    elif flag == 2: numb_type = 'c'
    else: numb_type = 'invalid flag'
    return numb_type

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_frac(value):
    st = value.split('/')
    if len(st) != 2: return False
    if st[0].replace(' ','0').replace('-','0').isdigit() and st[1].replace(' ','0').isdigit(): return True
    else: return False

def is_complex(value):
    try:
        complex(value)
        if complex(value).imag == 0: return False
        else: return True
    except ValueError:
        return False

def rc():
    return random.choice([-1, 1])

def get_value(flag):
    global numb_value
    if flag == 0:
        chck = True
        while(chck):
            chck = True
            if numb_type == 'r':  
                numb_value = input("Введите число = ")
                if is_float(numb_value) or is_frac(numb_value): chck = False
                else: print('Неверное число')
            if numb_type == 'c':  
                numb_value = input('Введите комплексное число >> ([a]+[b]j) = ')
                if is_complex(numb_value): chck = False
                else: print('Это не комплексное число')
    elif flag == 1:
        if rd == 0: numb_value = str(random.uniform(-10, 10))
        else: numb_value = f'{rc()*random.randint(1, 10)} {random.randint(1,9)}/{random.randint(1,9)}'
    elif flag == 2: numb_value = str(complex(rc()*random.randint(1, 10), rc()*random.randint(1, 10)))[1:-1]
    return numb_value

def get_oper(flag):
    global numb_oper
    op = ['+', '-', '*', '/']
    if flag == 0:
        chck = True
        while(chck): 
            chck = True
            numb_oper = input('Выберете операцию (+, -, * or /): ')
            if numb_oper in op: chck = False
    elif flag == 1 or flag == 2: numb_oper = op[random.randint(0,3)]
    return numb_oper 

def view_res(res):
    print(res)


def menu_collection(flag):
    get_type(flag)
    return (get_value(flag), get_value(flag), get_oper(flag))