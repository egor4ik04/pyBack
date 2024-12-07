'''
    Модуль с функциями 1-11 и 15, работающими со списками.
'''

import random

# 1. Функция, принимающая на вход список.
# Функция возвращает перевёрнутый список.
def reverse_list(input_list: list):
    '''Возвращает перевёрнутый список.'''
    return input_list[::-1]


# 2. Функция, принимающая на вход список.
# Функция изменяет одно, несколько или все значения списка.
# Функция возвращает изменённый список.
def modify_list(input_list):
    '''Удваивает числа и меняет строки на их верхний регистр.'''
    return [
        item * 2 if isinstance(item, (int, float))
        else item.upper() if isinstance(item, str)
        else item for item in input_list
    ]


# 3. Функция, принимающая на вход два или более списков.
# Функция сравнивает переданные на вход списки.
# Функция возвращает отметку, равны или нет все переданные на вход списки.
def compare_lists(*lists):
    '''Возвращает True, если все переданные списки равны, иначе False.'''
    return all(lst == lists[0] for lst in lists)


# 4. Функция, принимающая на вход список и доп. параметры (необходимо самостоятельно их определить).
# Функция ДОЛЖНА иметь возможность выбрать диапазон значений из переданного списка с заданным шагом.
# Нужно рассмотреть все возможные ситуации, связанные с передаваемыми значениями.
# Функция возвращает список, соответствующий диапазону.
def slice_list(input_list: list, start=0, end=None, step=1):
    '''Возвращает срез списка с заданными параметрами. start - включитально, end - нет.'''
    if end is None:
        end = len(input_list)
    return input_list[start:end:step]


# 5. Функция, принимающая на вход некие параметры.
# Функция создаёт список, основываясь на переданных параметрах.
# Создание списка, его наполнение и возврат полученного списка.
def create_string_list(*args, convert=True):
    '''Создаёт список, конвертируя элементы в строки, если параметр convert - True.'''
    if convert:
        return [str(item) for item in args]
    return [item for item in args]


# 6. Функция, принимающая на вход список и доп. параметры.
# Функция вставляет элемент в заданную позицию списка.
# Функция возвращает изменённый список.
def insert_element(input_list: list, element, position: int):
    '''Вставляет элемент в заданную позицию списка.
    Индекс position вне диапозона заменяется на конечный.'''
    if position < 0 or position > len(input_list):
        position = len(input_list)
    input_list.insert(position, element)
    return input_list


# 7. Функция, принимающая на вход два или более списков и доп. параметры.
# Функция объединяет все переданные на вход списки и сортирует их желаемым образом.
# Функция возвращает результирующий список.
def merge_and_sort(*lists, reverse=False, key=None):
    '''Объединяет все переданные списки и сортирует их.'''
    merged_list = []
    for lst in lists:
        if not isinstance(lst, list):
            lst = [lst]  # конверт в list, если элемент не list
        merged_list.extend(lst)
    if key:
        return sorted(merged_list, reverse=reverse, key=key)
    if reverse:
        return reverse_list(merged_list)
    return merged_list


# 8. Функция, не принимающая никаких параметров.
# Функция создаёт список из целых чисел произвольной длины.
# Функция проверяет, длина списка чётное число или нет.
# Если чётное, то функция сообщает об этом и создаёт новые списки
# до тех пор,пока не будет создан список нечётной длины.
# Если нечётное, то функция ищет центральный элемент списка и
# выводит количество элементов с таким же значением, что и у центрального элемента.
def generate_and_check_list():
    '''Создаёт список целых чисел произвольной длины и выводит центральное число 
    с количеством его повторов по всему списку, если число элементов нечётное.'''
    random_list = [random.randint(1, 9) for _ in range(random.randint(10, 100))]
    if len(random_list) % 2 == 0:
        print(f"Длина списка = {len(random_list)}. Повторная генерация.")
        return generate_and_check_list()
    else:
        central_element = random_list[len(random_list) // 2]
        count = random_list.count(central_element)
        print(f"""Длина списка = {len(random_list)}.
В центре = {central_element}.
Повторов '{central_element}' в списке = {count}""")
        return random_list


# 9. Функция, прибавляющая к первому списку другие списки.
# Если длина первого списка превышает заданный порог,
# необходимо удалить из списка некоторые элементы,
# чтобы число элементов списка не превышало порог.
# Функция возвращает изменённый первый список.
def add_and_limit_list(main_list: list, *other_lists, max_len=10):
    '''Прибавляет к первому списку другие списки и ограничивает длину списка по порогу.'''
    for lst in other_lists:
        if not isinstance(lst, list):
            lst = [lst]
        main_list.extend(lst)
    if len(main_list) > max_len:
        main_list = main_list[:max_len]
    return main_list


# 10. Минимум 6 функций, которые сортируют список по заданным критериям.
# Минимум 3 из этих функций ДОЛЖНЫ использовать функцию map().
def sort_by_digit_sum(numbers: list):
    '''Сортирует список чисел по сумме цифр числа.'''
    return sorted(numbers, key=lambda x: sum(map(int, str(abs(x)))))


def sort_by_vowel_length(strings: list):
    '''Сортирует список строк по длине строки, если строка начинается с гласной.'''
    vowels = "aeiouAEIOU"
    return sorted(strings, key=lambda x: len(x) if x[0] in vowels else 0)


def sort_by_abs_diff(numbers: list, target=50):
    '''Сортирует список чисел по абсолютной разнице от заданного числа (по умолчанию 50).'''
    return sorted(numbers, key=lambda x: abs(x - target))


def sort_by_vowel_count(strings: list):
    '''Сортирует список строк по количеству гласных в строке.'''
    vowels = "aeiouAEIOU"
    return sorted(strings, key=lambda x: sum(map(lambda c: c in vowels, x)))


def sort_by_first_letter(strings: list):
    '''Сортирует список строк по первой букве каждого слова в строке.'''
    return sorted(strings, key=lambda x: list(map(lambda word: word[0], x.split())) if x else [])


def sort_by_unique_chars(strings: list):
    '''Сортирует список строк по количеству уникальных символов в строках.'''
    return sorted(strings, key=lambda x: len(set(x)))


# 11. Функция, которая извлекает с удалением минимальный элемент списка.
# Функция возвращает минимальный элемент списка.
def remove_min_element(input_list: list):
    '''Извлекает с удалением минимальный элемент списка.'''
    if not input_list:
        raise ValueError("Список не может быть пустым")
    min_element = min(input_list)
    input_list.remove(min_element)
    return min_element


# 15. Функция, принимающая на вход один или несколько списков, и, возможно, доп. параметры.
# Функция формирует двумерный список по произвольным критериям и возвращает этот список.
def create_2d_list(*lists, fill_if_less=False, fill_value=None, max_length=None):
    '''Создаёт двумерный список из переданных списков с опциональным выравниванием.'''
    max_len = max(len(lst) for lst in lists) if max_length is None else max_length
    result = []
    for lst in lists:
        row = lst[:max_len]
        if fill_if_less and len(row) < max_len:
            row += [fill_value] * (max_len - len(row))
        result.append(row)
    return result
