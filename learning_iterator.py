# -*- coding: utf8 -*-

import abc

class Aggregate(abc.ABC):
	"""
	Абстрактный класс агрегатора.
	Должен содержать объекты к которым будет получать доступ итератор.
	"""
	@abc.abstractmethod
	def iterator(self):
		"""
		Возвращает итератор
		"""
		pass

class Iterator(abc.ABC):
	"""
	Абстрактный класс итератора.
	Позволяет обходить содержимое класса агрегатора.
	"""
	def __init__(self, collection, cursor):
		self._collection = collection
		self._cursor = cursor

	@abc.abstractmethod
	def first(self):
		"""
		Возвращает итератор к началу агрегата.
		Так же называют reset
		"""
		pass

	@abc.abstractmethod
	def next(self):
		"""
		Переходит на следующий элемент агрегата.
		Вызывает ошибку StopIteration, если достигнут конец последовательности.
		"""
		pass

	@abc.abstractmethod
	def current(self):
		"""
		Возвращает текущий элемент
		"""
		pass

class ListIterator(Iterator):
	def __init__(self, collection, cursor):
		"""
		:param collection: список
		:param cursor: индекс с которого начнется перебор коллекции.
		так же должна быть проверка -1 >= cursor < len(collection)
		"""
		super().__init__(collection, cursor)

	def first(self):
		"""
		Начальное значение курсора -1.
		Так как в нашей реализации сначала необходимо вызвать next
		который сдвинет курсор на 1.
		"""
		self._cursor = -1

	def next(self):
		"""
		Если курсор указывает на последний элемент, то вызываем StopIteration,
		иначе сдвинет курсор на 1.
		"""
		if self._cursor + 1 >= len(self._collection):
			raise StopIteration()
		self._cursor += 1

	def current(self):
		"""
		Возвращаем текущий элемент
		"""
		return self._collection[self._cursor]

class ListCollection(Aggregate):
	def __init__(self, collection):
		self._collection = list(collection)

	def iterator(self):
		return ListIterator(self._collection, -1)

print("Проверка итерируемого класса и самописного итератора")
collection = (1, 2, 5, 6, 8)
print("Создаем класс агрегатор")
aggregate = ListCollection(collection)
print("Определяем какой итератор будет использовать класс агрегатор")
itr = aggregate.iterator()
print("Начинаем обход элементов класса агрегатора")
while True:
	try:
		itr.next()
	except StopIteration:
		break
	print(itr.current())
print("Возвращаем итератор в начальное состояние")
itr.first()
print("Повторяем предыдущий обход")
while True:
	try:
		itr.next()
	except StopIteration:
		break
	print(itr.current())
'''
В стандартной библиотеке collections.abc.Iterable класс
class Iterable(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:
            return _check_methods(C, "__iter__")
        return NotImplemented
'''
print("Проверка класса с использование протокола итераторов Python")
print("Определение классов со встроенным протоколом итераторов")
import collections
class SomeIterable1(collections.abc.Iterable):
	def __iter__(self):
		pass

class SomeIterable2:
	def __iter__(self):
		pass

class SomeIterable3():
	def __init__(self):
		self._collection = (1, 2, 3, 4, 5)

	def __getitem__(self, key):
		return self._collection[key]
	
	def __enter__(self):
		return self._collection

	def __exit__(self, *args):
		pass

print("Является ли класс потомок Iterable итерируемым? ", isinstance(SomeIterable1(), collections.abc.Iterable))
print("Является ли класс c определенным методом __iter__ итерируемым? ", isinstance(SomeIterable2(), collections.abc.Iterable))
print("Является ли класс без метода __iter__ итерируемым ? ", isinstance(SomeIterable3(), collections.abc.Iterable))
print("Однако цикл for может ходить по нему, поскольку у него есть метод __getitem__")
with SomeIterable3() as e:
	for i in e:
		print(i)

print("Итерируемый объект, это объект, от которого встроенная функция iter() может получить итератор")
print("Итератор в python - это любой объект, реализующий метод __next__(or __getitem__()), который должен вернуть следующий объект или ошибку StopIteration,\
		также он реализует метод __iter__ и поэтому сам явл. итерируемым объектом")
print("getitem можно использовать когда у итерируемого класса нету в потомках abc.Iterator")

class ListIterator(collections.abc.Iterator):
	def __init__(self, collection, cursor = -1):
		self._collection = collection
		self._cursor = cursor

	def __next__(self):
		if self._cursor + 1 >= len(self._collection):
			raise StopIteration()
		self._cursor += 1
		return self._collection[self._cursor]

	def __getitem__(self, key):
		return self._collection[key]


class ListCollection(collections.abc.Iterable):
	def __init__(self, collection):
		self._collection = collection

	def __iter__(self):
		return ListIterator(self._collection, -1)

collection = (1, 2, 5, 6, 8)
aggregate = ListCollection(collection)

for item in aggregate:
    print(item)

for item in ListIterator((1,2,3,4,5)):
	print(item)

print("Все")
