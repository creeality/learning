# -*- coding: utf8 -*-

def decorator_1(func):
	def wrapper():
		print("decorator_1 начал работу")
		func()
		print("decorator_1 закончил работу")
	return wrapper

def decorator_2(func):
	def wrapper():
		print("decorator_2 начал работу")
		func()
		print("decorator_2 закончил работу")
	return wrapper

def decorator_3(func):
	def wrapper(arg1 : str, arg2 : str):
		print("decorator_3 начал работу")
		func(arg1, arg2)
		print("decorator_3 закончил работу")
	return wrapper

def decorator_4(func):
	def wrapper(*args, **kwargs):
		print("decorator_4 начал работу")
		func(*args, **kwargs)
		print("decorator_4 закончил работу")
	return wrapper

def test_func():
	print("Hello World!");

def test_func_1():
	print("Hello World!"[::-1])

@decorator_2
@decorator_1
def test_func_2():
	print("World Hello!")

@decorator_3
def test_func_3(arg1 : str, arg2 : str):
	print(arg1 + arg2)

@decorator_4
def test_func_4(*args, **kwargs):
	for i, arg in enumerate(args):
		print("*args {} : {}".format(i, arg))
	for i, key in enumerate(kwargs.keys()):
		print("**kwargs {} : {}:{}".format(i, key, kwargs[key]))

print("Проверка работы декораторы без сахара")
print("Функция без обертки")
test_func()
print("Функция с оберткой")
dec_test_func = decorator_1(test_func)
dec_test_func()
print("Подменяем оригинальную функцию, на обернутую функцию")
test_func = decorator_1(test_func)
test_func()
print("Функция обернутая двумя декораторами")
test_func_1 = decorator_2(decorator_1(test_func_1))
test_func_1()
print("Проверка работы декораторы c сахаром")
test_func_2()
print("Проверка передачи аргументов декорируемой функции")
test_func_3("Hello ", "World!")
print("Проверка передачи аргументов args, kwargs декорируемой функции")
test_func_4(1,2,3,4, test1=1, test2=2)
print("Все")
