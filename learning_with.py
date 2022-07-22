# -*- coding: utf8 -*-

class example_with(object):
	def __init__(self):
		print("Вызван конструктор")

	def __del__(self):
		print("Вызван деструктор")
	
	def __enter__(self):
		print("Вход в менеджер контекста")
		return self

	def __exit__(self, *args):
		print("Выход из менеджера контекста")
	
	def hello(self):
		print("Hello World!")

print("Вызов класса с кастомным менеджером контекста")
with example_with() as example:
	example.hello()
print("Все")
