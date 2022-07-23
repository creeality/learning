# -*- coding: utf8 -*-

class FibonacciGenerator:
	def __init__(self):
		self.prev = 0
		self.cur = 1
	
	def __next__(self):
		result = self.prev
		self.prev, self.cur = self.cur, self.prev + self.cur
		return result

	def __iter__(self):
		return self

	def __enter__(self):
		return self

	def __exit__(self, *args):
		pass

def fibonacci():
	prev, cur = 0, 1
	while True:
		yield prev
		prev, cur = cur, prev + cur

def chain(*iterables):
	for it in iterables:
		for i in it:
			yield i

def new_chain(*iterables):
	for it in iterables:
		yield from it

print("Простой генератор")
with FibonacciGenerator() as e:
	for i in e:
		print(i)
		if i > 100:
			break
print("Генератор через yield")
for i in fibonacci():
	print(i)
	if i > 100:
		break
print("Итерируемый объект через выражение")
print([x for x in range(0, 10)])
print("Генераторно выражение")
print((x for x in range(0, 10)))
print("Обход вложенных")
print(list(chain([1, 2, 3], {'A', 'S', 'D', 'F'}, '1234567890')))
print("Обход вложенных через yield from")
print(list(new_chain([1, 2, 3], {'A', 'S', 'D', 'F'}, '1234567890')))
print("Все")
