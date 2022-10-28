import logg as log

def get_div(x, y, i):
    if i == 1:
        log.result_logger(x / y)
        return x / y
    elif i == 2:
        log.result_logger(x // y)
        return x // y
    elif i == 3:
        log.result_logger(x % y)
        return x % y    
    else: print("Вы ввели неправильные данные")
    