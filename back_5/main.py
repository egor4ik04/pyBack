'''
    main-файл, откуда вызываю все функции с демонстрацией примеров.
'''

from list_funcs import (
    reverse_list,
    modify_list,
    compare_lists,
    slice_list,
    create_string_list,
    insert_element,
    merge_and_sort,
    generate_and_check_list,
    add_and_limit_list,
    sort_by_digit_sum,
    sort_by_vowel_length,
    sort_by_abs_diff,
    sort_by_vowel_count,
    sort_by_first_letter,
    sort_by_unique_chars,
    remove_min_element,
    create_2d_list
)

from tuple_funcs import (
    merge_tuples,
    min_in_tuples,
    get_types,
    check_element
)

from dict_funcs import (
    get_keys_where_value_more,
    invert_dictionary,
    remove_keys,
    count_key_matches,
    find_values_in_dict
)

# 19. Функция, вызывающая все другие функции из шагов 1-18
def main():
    '''Вызов всех функций.'''
    # 1. Функция, переворачивающая исходный список.
    print("\n1. reverse_list")
    my_list = [1, 2, 3, 4, 5]
    print(f">({my_list})")
    print(reverse_list(my_list))

    # 2. Функция, изменяющая значения списка.
    print("\n2. modify_list")
    my_list = [1, "hello", 3.5, "world"]
    print(f">({my_list})")
    print(modify_list(my_list))

    # 3. Функция, сравнивающая два или более списков.
    print("\n3. compare_lists")
    list_1 = [1, 2, 3]
    list_2 = [1, 2, 3]
    list_3 = [4, 5, 6]
    print(f">({list_1}, {list_2}, {list_3})")
    print(compare_lists(list_1, list_2, list_3))
    print(f">({list_1}, {list_2})")
    print(compare_lists(list_1, list_2))

    # 4. Функция, возвращающая диапазон значений из списка.
    print("\n4. slice_list")
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f">({my_list}, start=2, end=8, step=2)")
    print(slice_list(my_list, start=2, end=8, step=2))

    # 5. Функция, создающая список строк на основе переданных параметров.
    print("\n5. create_string_list")
    print(">(1, 2.5, True, 'hello')")
    print(create_string_list(1, 2.5, True, 'hello'))
    print(">(10, 'world', 3.14, False, 42, convert=False)")
    print(create_string_list(10, 'world', 3.14, False, 42, convert=False))

    # 6. Функция, вставляющая элемент в заданную позицию списка (при нарушении диапозона - в конец).
    print("\n6. insert_element")
    my_list = [1, 2, 3, 4, 5]
    print(f">({my_list}, 99, 99)")
    print(insert_element(my_list, 99, 99))
    print(f">({my_list}, 'start', 0)")
    print(insert_element(my_list, 'start', 0))

    # 7. Функция, объединяющая списки и сортирующая их.
    print("\n7. merge_and_sort")
    list1 = [3, 'list1', 4.5]
    list2 = ['list2', 8]
    list3 = [6, 'list3', 'test']
    print(f">({list1}, {list2}, {list3}, key=None)")
    print(merge_and_sort(list1, list2, list3, key=None))
    print(f">({list1}, {list2}, {list3}, reverse=True, key=lambda x: (len(str(x))))")
    print(f"{merge_and_sort(list1, list2, list3, reverse=True, key=lambda x: (len(str(x))))}")

    # 8. Функция повторно генерует список целых чисел, пока не найдёт центральный элемент.
    print("\n8. generate_and_check_list")
    print(">()")
    print(generate_and_check_list())
    print(">()")
    print(generate_and_check_list())

    # 9. Функция прибавляет к первому списку другие списки и ограничивает его длину.
    print("\n9. add_and_limit_list")
    list1 = [1, 515, 55]
    list2 = ['4', 5, 'he']
    list3 = ['ll', '0', False, 1.1, 11, [1, 515, 55]]
    print(f">({list1}, {list2}, {list3}, max_len=10)")
    print(add_and_limit_list(list1, list2, list3, max_len=10))

    # 10.1. Функция сортирует список чисел по сумме цифр.
    print("\n10.1. sort_by_digit_sum")
    list1 = [105, 21, 78, 456]
    print(f">({list1})")
    print(sort_by_digit_sum(list1))

    # 10.2. Функция сортирует список строк по длине, если строка начинается с гласной.
    print("\n10.2. sort_by_vowel_length")
    list2 = ["orange", "banana", "kiwi", "apple", "cherry"]
    print(f">({list2})")
    print(sort_by_vowel_length(list2))

    # 10.3. Функция сортирует список чисел по абсолютной разнице от 50.
    print("\n10.3. sort_by_abs_diff")
    print(f">({list1})")
    print(sort_by_abs_diff(list1))

    # 10.4. Функция сортирует список строк по количеству гласных в строке.
    print("\n10.4. sort_by_vowel_count")
    print(f">({list2})")
    print(sort_by_vowel_count(list2))

    # 10.5. Функция сортирует список строк по первой букве каждого слова.
    print("\n10.5. sort_by_first_letter")
    list2 = ["get func", "top 10", "full speed", "touch screen", "find letter a", "go again"]
    print(f">({list2})")
    print(sort_by_first_letter(list2))

    # 10.6. Функция сортирует список строк по количеству уникальных символов в строках.
    print("\n10.6. sort_by_unique_chars")
    print(f">({list2})")
    print(sort_by_unique_chars(list2))

    # 11. Функция извлекает с удалением минимальный элемент списка
    print("\n11. remove_min_element")
    my_list = [5, 3, 9, 1, 6]
    print(f">({my_list})")
    print(f"Минимальный элемент: {remove_min_element(my_list)}")
    print(f"Список после удаления: {my_list}")

    # 12.1. Функция объединяет несколько кортежей в один
    print("\n12.1. merge_tuples")
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    tuple3 = (7, 8)
    print(f">({tuple1}, {tuple2}, {tuple3})")
    print(merge_tuples(tuple1, tuple2, tuple3))

    # 12.2. Функция находит минимальный элемент среди всех элементов в нескольких кортежах
    print("\n12.2. min_in_tuples")
    tuple1 = (10.1, 20, 30)
    tuple2 = (5, 15, 25)
    tuple3 = (40, 50)
    print(f">({tuple1}, {tuple2}, {tuple3})")
    print(min_in_tuples(tuple1, tuple2, tuple3))

    # 13. Функция формирует кортеж из типов данных элементов входного кортежа.
    print("\n13. get_types")
    tuple1 = (42, "hello", 3.14, [1, 2, 3], {"key": "value"}, None)
    print(f">({tuple1})")
    print(get_types(tuple1))

    # 14. Функция проверяет, есть ли заданный элемент в кортеже.
    print("\n14. check_element")
    tuple1 = ("test", "hello", 42, False, 3.14)
    print(f">({tuple1}, 'Test', case_sensitive=False)")
    print(check_element(tuple1, 'Test', case_sensitive=False))
    print(f">({tuple1}, 'Test', case_sensitive=True)")
    print(check_element(tuple1, 'Test', case_sensitive=True))

    # 15. Функция формирует двумерный список из переданных списков.
    print("\n15. create_2d_list")
    list1 = [1, 2, 3]
    list2 = ["a", "b"]
    list3 = [True, False, True, False, False, False, True]
    print(f">({list1}, {list2}, {list3}, fill_if_less=True, fill_value='-', max_length=5)")
    print(create_2d_list(list1, list2, list3, fill_if_less=True, fill_value='-', max_length=5))
    print(f">({list1}, {list2}, {list3}, fill_if_less=False)")
    print(create_2d_list(list1, list2, list3, fill_if_less=False))

    # 16.1. Функция возвращает ключи словаря, значения которых больше порога.
    print("\n16.1. get_keys_over_limit")
    dict1 = {'a': 5, 'b': 10, 'c': 15}
    threshold = 8
    print(f">({dict1}, threshold={threshold})")
    print(get_keys_where_value_more(dict1, threshold))

    # 16.2. Функция инвертирует словарь.
    print("\n16.2. invert_dictionary")
    dict1 = {'one': 1, 'two': 2, 'three': 3}
    print(f">({dict1})")
    print(invert_dictionary(dict1))

    # 16.3. Функция удаляет элементы словаря с указанными ключами.
    print("\n16.3. remove_keys")
    dict1 = {'x': 1, 'y': 2, 'z': 3}
    keys_to_remove = ['x', 'z']
    print(f">({dict1}, keys_to_remove={keys_to_remove})")
    print(remove_keys(dict1, keys_to_remove))

    # 17. Функция считает количество вхождений ключа во всех словарях.
    print("\n17. count_key_occurrences")
    dict1 = {'name': 'Ivan', 'age': 25}
    dict2 = {'name': 'Petr', 'city': 'Moscow'}
    dict3 = {'age': 30, 'city': 'Kaluga'}
    key_to_count = 'name'
    print(f">({dict1}, {dict2}, {dict3}, key_to_count='{key_to_count}')")
    print(count_key_matches(dict1, dict2, dict3, key_to_count=key_to_count))

    # 18. Функция ищет значения в самом глубоком уровне вложенного словаря.
    print("\n18. find_values_in_nested_dict")
    nested_dict = {
        'level1a': {
            'level2a': {
                'level3': {
                    'target1': 'value1',
                    'other2': 'value2'
                }
            },
            'level2b': {
                'target3': 'value1'
            }
        },
        'level1b': {
            'level2': {
                'level3': {
                    'target4': 'value3'
                }
            },
            'target5': 'value1'
        },
        'level1c': {
            'level2': {
                'level3': {
                    'level4': {
                        'target6': 'value1'
                    }
                }
            }
        }
    }
    target_value = 'value1'
    print(f">({nested_dict}, target_value='{target_value}')")
    print(find_values_in_dict(nested_dict, target_value))


if __name__ == '__main__':
    main()
