"""
HW 5-3
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def get_file_info(value: str):
    some_file = value.split('\\')[-1]
    f_path = value.replace(some_file, '')
    f_name, f_format = some_file.split('.')
    return f_path, f_name, f_format


file_path = 'C:\Program Files (x86)\dotnet\shared\eula.txt'

print(get_file_info(file_path))

print()
print(*[get_file_info(file_path)[i] for i in range(3)], sep='\n')
