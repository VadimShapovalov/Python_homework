from cgitb import text
import excep as ex
import logg


def cal_compl(ls, i):
    ls = ls.split()
    in_real_1 = float(ls[0])
    in_imag_1 = float(ls[1])
    a = complex(in_real_1, in_imag_1)
    print(a)
    in_real_2 = float(ls[2])
    in_imag_2 = float(ls[3])
    b = complex(in_real_2, in_imag_2)
    print(b)
    if i == "+":
        # logg.result_logger(a + b)
        return complex(a + b)
    elif i == "-":
        # logg.result_logger(a - b)
        return complex(a - b)
    elif i == "*":
        # logg.result_logger(a * b)
        return complex(a * b)
    elif i == "/" and b != 0:
        # logg.result_logger(a / b)
        return complex(a / b)
    elif i == "/" and b == 0:
        print("На ноль делить нельзя")
        text = "Пользователь ввел: 0. Это некорректный ввод"
        logg.actions_logger(text)
    elif i == "^":
        # logg.result_logger(a ** b)
        return complex(a ** b)

