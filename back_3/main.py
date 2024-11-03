'''
    Написать следующие конструкции:
        функция без параметров
        функция с параметрами
        функция с несколькими параметрами со значениями по умолчанию
        функция с несколькими параметрами, у которых задан тип
        функция с неопределённым количеством параметров (args)
        функция с неопределённым количеством параметров (kwargs)
        функция, вызывающая внутри себя другую функцию
        функция, принимающая функцию как параметр (минимум 3 примера)
        функция с объявленной внутри локальной функцией (минимум 2 примера)
        лямбда-выражение без параметров
        лямбда-выражение с параметрами
        функция, принимающая лямбда-выражение как параметр, 
            и вызывающая лямбда-выражение внутри себя
        функция с замыканиями (минимум 3 примера)
'''


import random
from param_funcs import (get_start_message, char_mixer, greet_user,
    generate_tag, get_sorted_list_str, build_profile)
from local_operate_funcs import (generate_random_tag, filter_list,
    transform_list, conditional_operation, is_prime, sum_list)
from lambda_funcs import (get_no_param_lambda, create_multiplier, process_value)
from closure_funcs import (counter, list_writer, create_prefixer)

if __name__ == "__main__":
    print("функция без параметров")
    print(get_start_message())
##########################################################################
    print("\nфункция с параметрами")
    print(char_mixer("Hello ", "world"))
##########################################################################
    print("\nфункция с несколькими параметрами со значениями по умолчанию")
    print(greet_user())
    print(greet_user(greeting="Здравствуйте", name="Хозяин"))
##########################################################################
    print("\nфункция с несколькими параметрами, у которых задан тип")
    print("Выбран титул", generate_tag(1, 4))
    print("Выбран титул", generate_tag(2, 1))
##########################################################################
    print("\nфункция с неопределённым количеством параметров (args)")
    inventory = ["яблоко", "меч", "зелье лечения"]
    print("инвентарь:")
    print(inventory)
    print("инвентарь (обработанный):")
    print(get_sorted_list_str(*inventory))
##########################################################################
    print("\nфункция с неопределённым количеством параметров (kwargs)")
    print(build_profile(name="Истер", tag=generate_tag(5, 4),
                        char_class="Паладин", age=34))
##########################################################################
    print("\nфункция, вызывающая внутри себя другую функцию")
    print("Случайный титул:", generate_random_tag())
##########################################################################
    print("\nфункция, принимающая функцию как параметр (минимум 3 примера)")
    def get_vovels(string_line):
        """Возвращает строку, содержащую только гласные из переданной строки."""
        vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
        result = ''.join([v for v in string_line if v in vowels])
        return result
    def get_consonants(string_line):
        """Возвращает строку, содержащую только согласные  из переданной строки."""
        consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
        result = ''.join([c for c in string_line if c in consonants])
        return result
    tag = generate_random_tag()
    print(f"Получаем из строки \"{tag}\" гласные")
    print(filter_list(tag, get_vovels))
    print(f"Получаем из строки \"{tag}\" согласные")
    print(filter_list(tag, get_consonants))
    def move_numbers(num_str):
        '''Сдвиг в строке всех цифр на следующее значение'''
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if num_str in numbers:
            if numbers.index(num_str)<len(numbers):
                result = numbers[numbers.index(num_str)+1]
            else:
                result = numbers[0]
        else:
            result = num_str
        return result
    print(''.join(transform_list("test123 5@4", move_numbers)))
    stat_strength: int = 10
    stat_agility: int = 8
    stat_xp: int = 2
    def strength_up(strength, agility):
        '''Повышение силы на 2 за счёт 1 ловкости'''
        return strength + 2, agility - 1
    def agility_up(strength, agility):
        '''Повышение ловкости на 2 за счёт 1 силы'''
        return strength - 1, agility + 2
    print("Статы персонажа сейчас:\n", build_profile(
        name="Тестер", strength=stat_strength, agility=stat_agility, xp=stat_xp))
    print("Распределяем очки опыта")
    while stat_xp > 0:
        stat_xp -= 1
        condition = random.randint(0, 1) > 0
        stat_strength, stat_agility = conditional_operation(
            stat_strength, stat_agility, condition, strength_up, agility_up)
    print("Новые статы персонажа:\n", build_profile(
        name="Тестер", strength=stat_strength, agility=stat_agility, xp=stat_xp))
##########################################################################
    print("\nфункция с объявленной внутри локальной функцией (минимум 2 примера)")
    print("Проверка на простое число:")
    print(f"5 : {is_prime(5)}")
    print(f"29 : {is_prime(29)}")
    print(f"78 : {is_prime(78)}")
    print("Вычисление суммы элементов списка:")
    nums = [1, 2, 3]
    print(f"{nums} : {sum_list(nums)}")
    nums = [24, 666, -191, 0, 1.1]
    print(f"{nums} : {sum_list(nums)}")
##########################################################################
    print("\nлямбда-выражение без параметров")
    no_param_lambda = get_no_param_lambda()
    no_param_lambda()
##########################################################################
    print("\nлямбда-выражение с параметрами")
    double = create_multiplier(2)
    triple = create_multiplier(3)
    print("Удвоим значения одной лямбдой и утроим другой")
    print(f"3 | {double(3)} | {triple(3)}")
    print(f"16 | {double(16)} | {triple(16)}")
    print(f"-5 | {double(-5)} | {triple(-5)}")
##########################################################################
    print("\nфункция, принимающая лямбда-выражение как параметр,",
            "и вызывающая лямбда-выражение внутри себя")
    print("С помощью функции передадим ранее полученную лямбду",
          "double как аргумент 1ый раз, и во 2ой запишем \"свежую\"")
    print(process_value(9, double))
    print(process_value(9, lambda x: x ** 3))
##########################################################################
    print("\nфункция с замыканиями (минимум 3 примера)")
    print("Функция, считающая, сколько раз её вызвали")
    call = counter()
    for x in range(0, 5):
        print("Вызов счётчика", call())
    print("Функция, позволяющая записывать строки и получать их")
    my_list = list_writer()
    print(f"my_list(1) -> {my_list(1)}")
    print(f"my_list(5, \"восславь Солнце!\") -> {my_list(5, "восславь Солнце!")}")
    print(f"my_list(5) -> {my_list(5)}")
    print("Вызов счётчика", call())
    print("Создадим функцией префикс для пользователей (@) и команд (!)")
    user_prefixer = create_prefixer("@")
    command_prefixer = create_prefixer("!")
    print("Обработаем соответствующие цели:")
    print(f"user_prefixer(\"Bob_47\") -> {user_prefixer("Bob_47")}")
    print(f"command_prefixer(\"cheats true\") -> {command_prefixer("cheats true")}")
    print(f"command_prefixer(\"restart\") -> {command_prefixer("restart")}")
