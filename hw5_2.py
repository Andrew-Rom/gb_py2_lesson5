"""
HW 5-2
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел, начиная с числа 2.
✔ Для проверки числа на простоту используйте правило:
  «число является простым, если делится нацело только на единицу и на себя».
"""


def gen_simple_num(qty: int, number=2):
    simple_numbers = [number]
    number_is_simple = False
    while len(simple_numbers) < qty:
        number += 1
        for dev in range(2, number):
            if number % dev == 0:
                break
        else:
            number_is_simple = True
        if number_is_simple:
            simple_numbers.append(number)
            number_is_simple = False
    yield simple_numbers


n = 15
print(*gen_simple_num(n))
print(gen_simple_num(n))
print(type(gen_simple_num))
