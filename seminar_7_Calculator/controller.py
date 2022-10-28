import user_interface as us
import excep as ex
import logg
import model_div as div
import model_sub as sub
import model_sum as sum
import model_mult as mult
import compl
import sys


def main():
	us.main_menu("Welcome")
	while(True):
		us.main_menu("Menu")
		i = ex.digit()
		if i == 1: 
			print('Калькулятор для работы с рациональными числами')
			us.choice_actions_menu("Рациональные числа")
			i = ex.action()
			
			if i == "+":
				logg.entered_logger('Сложение')
				print("Результат: ", sum.get_sum(ex.digit_number('1ое число: '), ex.digit_number('2ое число: ')))
			elif i == "-":
				logg.entered_logger('Вычитание')
				print("Результат: ",sub.get_sub(ex.digit_number('1ое число: '), ex.digit_number('2ое число: ')))
			elif i == "*":
				while True:
					us.choice_mult_actions('Умножение')
					i = ex.digit()
					if i == 1:
						print("Результат: ",mult.get_mult(ex.digit_number('1ое число: '), ex.digit_number('2ое число: '),i))
						break
					elif i == 2:
						print("Результат: ",mult.get_mult(ex.digit_number('1ое число: '), ex.digit_number('2ое число: '),i))
						break
					else:
						print('=' * 30)
						print("Введите одно из заданных значений")
						print('=' * 30)
			elif i == "/": 
				while True:
					us.choice_div_actions('Деление')
					i = ex.digit()
					if i == 1:
						print("Результат: ",div.get_div(ex.digit_number('1ое число: '), ex.zero_number('2ое число: '),i))
						break
					elif i == 2:
						print("Результат: ",div.get_div(ex.digit_number('1ое число: '), ex.zero_number('2ое число: '),i))
						break
					elif i == 3:
						print("Результат: ",div.get_div(ex.digit_number('1ое число: '), ex.zero_number('2ое число: '),i))
						break
					else:
						print('=' * 30)
						print("Введите одно из заданных значений")
						print('=' * 30)
			elif i == "5":
				ex.mistake('Завершение работы')
				print('---------------------------------------------')
				print("Программа завершила работу")
				print('---------------------------------------------')
				break
			else: 
				ex.mistake()
				us.end_menu("Exit the app")
				if(ex.digit() == 2):
					print('---------------------------------------------')
					print("Программа завершила работу")
					print('---------------------------------------------')
					break
					
		elif i == 2:
			print('Калькулятор для работы с комплексными числами')
			us.choice_actions_menu("Комплексные числа")
			i = ex.action()
			if i == '5': 
				print('---------------------------------------------')
				print("Программа завершила работу")
				print('---------------------------------------------')
				break
			print(compl.cal_compl(i))
			
		elif i == 3:
			us.end_menu("Exit the app")
			while True:
				i = ex.digit()
				if i == 1:
					break
				elif i == 2: 
					print('---------------------------------------------')
					print("Программа завершила работу")
					print('---------------------------------------------')
					sys.exit()
				else:
					print('---------------------------------------------')
					print("Введите одно из заданных значений")
					print('---------------------------------------------') 	
		else:
			print('---------------------------------------------')
			print("Введите одно из заданных значений")
			print('---------------------------------------------')
            