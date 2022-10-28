import logg

def get_mult(x, y, i):
    if i == 1:
        logg.result_logger(x * y)
        return x * y
    elif i == 2:
        logg.result_logger(x ** y)
        return x ** y
    else: print("Вы ввели неправильные данные")   
