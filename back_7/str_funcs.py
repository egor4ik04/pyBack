'''
    В данном можуле реализованы функции по работе со строками из заданий 1-9
'''

import random

# 1. Функция, принимающая на вход некий набор параметров (минимум 3 параметра).
# Внутри себя эта функция содержит заранее определённую строку,
# в которую можно подставлять значения переменных.
# Функция возвращает строку, в которую вставлены значения, такие что
# 1.1. Как минимум, одно значение - это просто строка
# 1.2. Как минимум, одно значение - это результат арифметической операции
# 1.3. Как минимум, одно значение - это результат вызова другой функции
def rand_multiply_sum(name: str, amount: float, min_rand: float, max_rand: float):
    '''Возвращает сообщение с информацией о ставке игрока и случайным изменением баланса.'''
    return f"""{name} ставит сумму: {amount}.
Диапозон изменения баланса: {min_rand * amount} .. {max_rand * amount}.
{name} получает {amount * random.uniform(min_rand, max_rand):.2f}"""


# 2. Функция, которая формирует строку, состоящую из повторений комбинации других строк.
# Эта функция выводит получившуюся строку, где каждое повторение выводится на отдельной строке.
def repeat_strings(strs: list[str], repeats: int):
    '''Возвращает строку из повторений комбинации строк, каждое повторение - на новой строке.'''
    result = '\n'.join(''.join(strs) for _ in range(repeats))
    return result


# 3. Функция, которая считает количество вхождений подстроки в строку без учёта регистра.
def count_substring_ignore_reg(main_string: str, substring: str):
    '''Считает количество вхождений подстроки в строку без учёта регистра.'''
    return main_string.lower().count(substring.lower())


# 4. Функция, принимающая на вход строку и выводящая подстроку, содержащуюся между двумя индексами.
# Индексы ДОЛЖНЫ быть больше нуля и меньше длины строки минус 1.
# Тело функции ДОЛЖНО быть написано в одну строку.
def substring_between_indices(string: str, start: int, end: int):
    '''Возвращает подстроку из строки между указанными индексами.'''
    return string[start:end] if 0 <= start < len(string) and 0 < end <= len(string) else ''
# Для примеров я сделал <= и >= на концах, чтобы был смысл в выводе не пустой строки,
# иначе же и так выведется пустая


# 5. Функция, принимающая на вход произвольное количество разных строк,
# где содержатся любые кириллические буквы, а также могут содержаться латинские буквы,
# но только такие, которые визуально неотличимы от кириллических. Регистр букв произвольный.
# Эта функция ищет слова, в которых содержатся латинские буквы.
# На выход возвращаются строки, где были обнаружены латинские символы и количество слов,
# в которых была обнаружена хотя бы одна латинская буква.
def find_words_with_latin(*strings: str):
    '''Ищет слова с латинскими буквами и возвращает строки с такими словами и их количество.'''
    latin_similar_letters = 'AaEeKMOoPpCcTXxyHB'
    search = []
    for string in strings:
        words = string.split()
        for word in words:
            if any(char in latin_similar_letters for char in word):
                search.append((string, word))
    return search, len(search)


# 6. Функция, определяющая, является ли строка палиндромом (одинаково читается с начала и с конца).
# Строка МОЖЕТ содержать как цифры, так и буквы.
def is_palindrome(s: str):
    '''Проверяет, является ли строка палиндромом, игнорируя регистр и пробелы.'''
    s = ''.join(e.lower() for e in s if e.isalnum())
    return s == s[::-1]


# 7. Функция, принимающая на вход строку, содержащую несколько слов,
# которые разделены одним или несколькими пробелами.
# У входной строки могут быть несколько пробелов в начале и в конце.
# Функция убирает лишние пробелы: то есть все пробелы в начале и в конце строки,
# а между словами оставляет только один пробел.
# Функция возвращает длину строки после удаления лишних пробелов.
def remove_extra_spaces(s: str):
    '''Удаляет лишние пробелы в строке и возвращает длину строки после изменения.'''
    s = ' '.join(s.split())
    return len(s)


# 8. Функция, принимающая на вход строку, содержащую текст из нескольких предложений.
# Функция заменяет символы окончания предложения на символ переноса строки.
# Функция возвращает получившуюся строку.
def replace_sentence_endings(text: str):
    '''Заменяет окончания предложений на перенос строки.'''
    text = text.replace('... ', '\n').replace('. ', '\n').replace('! ', '\n').replace('? ', '\n')
    text = text.replace('...', '\n').replace('.', '\n').replace('!', '\n').replace('?', '\n')
    return text


# 9. Минимум 3 функции, содержащие произвольные алгоритмы работы со строками.
# Функции ДОЛЖНЫ решать алгоритмы, отличные от реализованных в п. 1-8
def contains_only_digits_word(text: str):
    '''Проверяет, есть ли в строке хотя бы одно слово, состоящее только из цифр.'''
    words = text.split()
    return any(word.isdigit() for word in words)


def contains_anagram(text: str):
    '''Проверяет, есть ли в строке хотя бы одно слово, которое является анаграммой другого.'''
    words = text.split()
    for i, let1 in enumerate(words):
        for let2 in words[i + 1:]:
            if sorted(let1.lower()) == sorted(let2.lower()):
                return True
    return False


def remove_vowels(text: str):
    '''Удаляет все гласные из строки.'''
    vowels = 'аеёиоуэюяАЕЁИОУЭЮЯ'
    return ''.join(char for char in text if char not in vowels)
