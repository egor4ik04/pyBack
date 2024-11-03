'''
    функция без параметров
    функция с параметрами
    функция с несколькими параметрами со значениями по умолчанию
    функция с несколькими параметрами, у которых задан тип
    функция с неопределённым количеством параметров (args)
    функция с неопределённым количеством параметров (kwargs)
'''


import random


# Функция без параметров
def get_start_message():
    """Выводит начальное сообщение."""
    return "Программа запущена!"


# Функция с параметрами
def char_mixer(first_part, second_part):
    """Перемешивает все символы в строках, предварительно складывая их в одну."""
    a = list(str(first_part) + str(second_part))
    random.shuffle(a)
    return ''.join(a)


# Функция с несколькими параметрами со значениями по умолчанию
def greet_user(name="Гость", greeting="Привет"):
    """Приветствие пользователя с указанием шаблона приветствия и имени."""
    return f"{greeting}, {name}!"


# Функция с несколькими параметрами, у которых задан тип
def generate_tag(first_part_id: int, second_part_id: int) -> str:
    """Выдаёт словосочетание для тега, опираясь на выбранные положительные id,
        иначе рандомизирует."""
    frst_tags = ["мудрый", "всевидящий", "скромный", "выдающийся",
                     "мистер", "павший", "неугомонный", "безмолвный"]
    scnd_tags = ["лорд", "воин", "чудак", "старец", "генерал",
                     "цветок", "странник", "механизм", "ангел"]
    frst_part = frst_tags[first_part_id % len(frst_tags)
    ] if first_part_id >= 0 else frst_tags[random.randint(0, len(frst_tags)-1)]
    scnd_part = scnd_tags[second_part_id % len(scnd_tags)
    ] if second_part_id >= 0 else scnd_tags[random.randint(0, len(scnd_tags)-1)]
    return frst_part + " " + scnd_part


# Функция с неопределённым количеством параметров (args)
def get_sorted_list_str(*args):
    """Возвращает список переданных предметов в виде отсортированной строки."""
    a = sorted(args)
    return str(', '.join(a))


# Функция с неопределённым количеством параметров (kwargs)
def build_profile(name, **kwargs):
    """Создаёт профиль персонажа с поддержкой кастомных данных."""
    result = f"character profile:\n\tname: {name}"
    for key, value in kwargs.items():
        result += f"\n\t{key}: {value}"
    return result
