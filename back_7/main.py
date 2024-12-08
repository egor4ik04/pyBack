'''
    main-файл, откуда вызываю все функции с демонстрацией примеров.
'''

from str_funcs import (
    rand_multiply_sum,
    repeat_strings,
    count_substring_ignore_reg,
    substring_between_indices,
    find_words_with_latin,
    is_palindrome,
    remove_extra_spaces,
    replace_sentence_endings,
    contains_only_digits_word,
    contains_anagram,
    remove_vowels
)

# 10. Функция, которая последовательно вызывает ВСЕ вышесозданные функции.
# Функция ДОЛЖНА завершаться корректно и НЕ ДОЛЖНА иметь необработанных исключений
def main():
    '''Вызов всех функций.'''
    # 1. Функция сбора строки рассчёта случайного изменения значения суммы
    print("\n1. rand_multiply_sum")
    print(">('Test User', 100, -2.5, 2.5)")
    print(rand_multiply_sum('Test User', 100, -2.5, 2.5))

    # 2. Функция повторения комбинации строк с новой строкой для каждого повтора
    print("\n2. repeat_strings")
    print(">(['ABC', '123'], 3)")
    print(repeat_strings(['ABC', '123'], 3))
    print(">(['Hello', '-', 'World'], 5)")
    print(repeat_strings(['Hello', '-', 'World'], 5))

    # 3. Функция подсчёта вхождений подстроки без учёта регистра
    print("\n3. count_substring_ignore_case")
    print(">('Hello World, HELLO Universe', 'hello')")
    print(count_substring_ignore_reg('Hello World, HELLO Universe', 'hello'))
    print(">('We live while we feel aLIVE', 'Live')")
    print(count_substring_ignore_reg('We live while we feel aLIVE', 'Live'))

    # 4. Получение подстроки между индексами
    print("\n4. substring_between_indices")
    print(substring_between_indices('Hello, World!', 0, 5))
    print(">('Brainstorming', 3, len('Brainstorming')-3)")
    print(substring_between_indices('Brainstorming', 3, len('Brainstorming')-3))
    print(">('Space rocket', 2, 10)")
    print(substring_between_indices('Space rocket', 2, 10))

    # 5. Поиск слов с латинскими буквами
    print("\n5. find_words_with_latin")
    print(">('Тестовое сoобщение'," +
          "'Где-то здеcь запрятался шпиoн', 'абсолютно кириллическая строкa')")
    result, count = find_words_with_latin('Тестовое сoобщение', 
    'Где-то здеcь запрятался шпиoн', 'абсолютно кириллическая строкa')
    print(f"Строки с латинскими буквами всего {count}: {result}")

    # 6. Проверка на полиндром
    print("\n6. is_palindrome")
    print(">('Hello, World!')")
    print(is_palindrome('Hello, World!'))
    print(">('Was it a car or a cat I saw?')")
    print(is_palindrome('Was it a car or a cat I saw?'))

    # 7. Функция, убирающая лишние пробелы в строке
    print("\n7. remove_extra_spaces")
    print(">('  Это    строка с  лишними пробелами   ')")
    print(remove_extra_spaces('  Это    строка с  лишними пробелами   '))  # 39 -> 30
    print(">('Нет лишних пробелов!')")
    print(remove_extra_spaces('Нет лишних пробелов!'))  # 20 -> 20

    # 8. Функция, заменяющая окончания предложений на перенос строки
    print("\n8. replace_sentence_endings")
    print(">('Ночь...Улица. Фонарь? Аптека!')")
    print(replace_sentence_endings('Ночь...Улица. Фонарь? Аптека!'))

    # 9.1. Функция, которая проверяет, есть ли в строке хотя бы одно слово, состоящее только из цифр
    print("\n9.1. contains_only_digits_word")
    print(">('password 123')")
    print(contains_only_digits_word('password 123'))
    print(">('password cool132')")
    print(contains_only_digits_word('password cool132'))

    # 9.2. Функция, которая проверяет, есть ли в строке слова-анаграммы друг друга
    print("\n9.2. contains_anagram")
    print(">('Listen silent')")
    print(contains_anagram('Listen silent'))
    print(">('Hello world')")
    print(contains_anagram('Hello world'))

    # 9.3. Функция, которая возвращает строку с удалением всех гласных букв
    print("\n9.3. remove_vowels")
    print(">('Привет, как у тебя дела? Если не мешаю, давай поболтаем!')")
    print(remove_vowels('Привет, как у тебя дела? Если не мешаю, давай поболтаем!'))


if __name__ == '__main__':
    main()
