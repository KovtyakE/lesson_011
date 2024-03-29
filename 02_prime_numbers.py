# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#     def __init__(self, n):
#         self.values = n
#
#     def __iter__(self):
#         self.prime_numbers = []
#         self.value = 1
#         return self
#
#     def __next__(self):
#         if self.value < self.values:
#             self.value += 1
#             if self.prime_numbers == []:
#                 self.prime_numbers.append(self.value)
#                 return self.value
#             else:
#                 for num in self.prime_numbers:
#                     if self.value % num == 0:
#                         break
#                     elif num == self.prime_numbers[-1]:
#                         self.prime_numbers.append(self.value)
#                         return self.value
#                 # return ('Не является простым:' + str(self.value))
#
#         else:
#             raise StopIteration()
#
#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     if number is not None:
#         print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    value = 1
    prime_numbers = []
    while value < n:
        value += 1
        if not prime_numbers:
            prime_numbers.append(value)
            yield value
        for num in prime_numbers:
            if value % num == 0:
                if value is not num:
                    break
            elif num == prime_numbers[-1]:
                prime_numbers.append(value)
                yield value


for number in prime_numbers_generator(n=10000):
    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
