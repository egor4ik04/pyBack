'''
    Модуль с функциями 16-18, работающими со словарями.
'''

# 16. Минимум 3 функции, которые принимают на вход словарь.
# Функции совершают некие операции над словарём.
# Функции возвращают какое-либо значениЕ, значениЯ.
def get_keys_where_value_more(input_dict: dict, limit):
    '''Возвращает ключи, значения которых превышают порог.'''
    return [key for key, value in input_dict.items() if value > limit]


def invert_dictionary(input_dict: dict):
    '''Инвертирует словарь.'''
    return {value: key for key, value in input_dict.items()}


def remove_keys(input_dict: dict, keys_to_remove: list):
    '''Удаляет из словаря элементы с указанными ключами.'''
    return {key: value for key, value in input_dict.items() if key not in keys_to_remove}


# 17. Функция, принимающая на вход два или более словарей
# и доп. параметры (необходимо самостоятельно их определить).
# Функция считает, сколько раз встречается элемент
# с определённым ключом во всех словарях суммарно и выводит это значение.
def count_key_matches(*dicts, key_to_count):
    '''Считает, сколько раз встречается заданный ключ в словарях.'''
    return sum(1 for dict in dicts if key_to_count in dict)


# 18. Функция, принимающая на вход комплексный словарь определённого формата,
# у которого будет минимум 3 уровня вложенности.
# Функция ищет в этом словаре определённый элемент или элементы,
# располагающиеся на самом последнем уровне вложенности.
# Функция возвращает значение найденного элемента или элементов или None,
# если такой элемент или элементы не найдены.
def find_values_in_dict(input_dict: dict, target_value):
    '''Ищет значения на самом последнем уровне вложенного словаря.'''
    def recursive_search(d, value):
        if isinstance(d, dict):
            filtered = {}
            for k, v in d.items():
                if isinstance(v, dict):
                    sub_result = recursive_search(v, value)
                    if sub_result:
                        filtered[k] = sub_result
                elif v == value:
                    filtered[k] = v
            return filtered if filtered else None
        return None
    return recursive_search(input_dict, target_value)
