"""
✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт» без перехода на новую строку.
"""

print('ТАБЛИЦА УМНОЖЕНИЯ'.center(73))

tab_gen = (f'{m + c} x {n:<2} = {(n) * (m + c):>2}' for c in range(0, 5, 4) for n in range(2, 11) for m in range(2, 6))

print('', *[' '.join([' '.join([next(tab_gen) + '\t\t' for _ in range(4)]) # create line
                                                + '\n' for _ in range(9)]) # create block
                                                + '\n' for _ in range(2)]) # create tab