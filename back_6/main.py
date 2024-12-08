'''
    Глав. файл для общей демонстрации всех сделанных функций и иных конструкций.
'''

from file_common import (
    module_file_test,
    generate_password,
    random_selection,
    calculate_hypotenuse,
    degrees_to_radians,
    sin_and_cos_from_radians,
    set_locale_and_get_name,
    format_number_with_locale,
    format_currency_with_locale,
    set_precision_and_add,
    format_decimal_to_string,
    describe_character,
    total_inventory_weight,
    get_skill_levels,
    level_up_skill,
    create_character,
    GameCharacter,
    InventoryItem,
    Skill,
)

# 10. Функция, вызывающая все функции из шагов 2-9
def main():
    '''Вызов всех функций.'''
    # 1. выполнен в файлах file1-7.py и вызываетсяв файле file_common.py в пункте 2.
    # 3. расписан в file_common.py

    #2. Вывод древа функций из модулей
    print("4.1. generate_password")
    print(">()")
    module_file_test()

    # 4.1. Генерация пароля
    print("4.1. generate_password")
    print(">(10)")
    print({generate_password(10)})
    print(">(6)")
    print({generate_password(6)})

    # 4.2 Случайный выбор элементов
    print("\n4.2. random_selection")
    rand_terms = [
        'vscode', 'debugging', 'refactoring', 'lab',
        'server', 'client', 'frontend', 'backend', 'pixel', 'shader'
    ]
    print(f">({rand_terms, 3})")
    print(random_selection(rand_terms, 3))
    print(f">({rand_terms, 5})")
    print(random_selection(rand_terms, 5))

    # 5.1 Вычисление гипотенузы
    print("\n5.1. calculate_hypotenuse")
    print(">(3, 4)")
    print(calculate_hypotenuse(3, 4))
    print(">(5, 12)")
    print(calculate_hypotenuse(5, 12))

    # 5.2 Преобразование угла в радианы
    print("\n5.2. degrees_to_radians")
    print(">(30)")
    print(degrees_to_radians(30))
    print(">(32)")
    print(degrees_to_radians(32))
    print(">(60)")
    print(degrees_to_radians(60))

    # 5.3 Синус и косинус угла в радианах
    print("\n5.3. sin_and_cos_from_radians")
    print(f">({degrees_to_radians(30)})")
    print(sin_and_cos_from_radians(degrees_to_radians(30)))
    print(f">({degrees_to_radians(32)})")
    print(sin_and_cos_from_radians(degrees_to_radians(32)))
    print(f">({degrees_to_radians(60)})")
    print(sin_and_cos_from_radians(degrees_to_radians(60)))

    # 6.1 Установка локали и получение её имени
    print("\n6.1. set_locale_and_get_name")
    print(">('en_US.UTF-8')")
    print(set_locale_and_get_name('en_US.UTF-8'))
    print(">('ru_RU.UTF-8')")

    # 6.2 Форматирование числа с учётом локали
    print("\n6.2. format_number_with_locale")
    print(set_locale_and_get_name('en_US.UTF-8'))
    print(">(1234567.89)")
    print(format_number_with_locale(1234567.89))
    print(set_locale_and_get_name('ru_RU.UTF-8'))
    print(">(9876543.21)")
    print(format_number_with_locale(9876543.21))

    # 6.3 Форматирование валюты с учётом локали
    print("\n6.3. format_currency_with_locale")
    print(">(1234567.89, 'en_US.UTF-8')")
    print(format_currency_with_locale(1234567.89, 'en_US.UTF-8'))
    print(">(1234567.89, 'fr_FR.UTF-8')")
    print(format_currency_with_locale(1234567.89, 'fr_FR.UTF-8'))
    print(">(1234567.89, 'ru_RU.UTF-8')")
    print(format_currency_with_locale(1234567.89, 'ru_RU.UTF-8'))

    # 7.1 Установка точности и сложение
    print("\n7.1. set_precision_and_add") # точность - третий параметр
    print(">(2.5, 3.7, 5)")
    print(set_precision_and_add(2.5, 3.7, 5))
    print(">(1.123456, 2.654321, 10)")
    print(set_precision_and_add(1.123456, 2.654321, 10))

    # 7.2 Форматирование числа в строку с заданной точностью
    print("\n7.2. format_decimal_to_string")
    print(">(3.1415926535, 2)")
    print(format_decimal_to_string(3.1415926535, 2))
    print(">(123.456789, 4)")
    print(format_decimal_to_string(123.456789, 4))

    # 8. data-классы объявлены в file_common.py

    # 9.1 Передача объекта data-класса как параметр
    print("\n9.1. describe_character")
    character = GameCharacter(name="Archer", health=120, mana=80)
    print(f">({character})")
    print(describe_character(character))

    # 9.2 Работа со списком из объектов data-классов
    print("\n9.2. total_inventory_weight")
    inventory = [
        InventoryItem(item_name="Potion", quantity=3, weight=0.5),
        InventoryItem(item_name="Sword", quantity=1, weight=3.0),
    ]
    print(f">({inventory})")
    print(total_inventory_weight(inventory))

    # 9.3 Работа со словарём, где значение — объект data-класса
    print("\n9.3. get_skill_levels")
    skills = {
        "Archery": Skill(skill_name="Archery", level=2, experience=75.0),
        "Alchemy": Skill(skill_name="Alchemy", level=5, experience=50.0),
    }
    print(f">({skills})")
    print(get_skill_levels(skills))

    # 9.4 Модификация значений объекта data-класса
    print("\n9.4. level_up_skill")
    skill = Skill(skill_name="Stealth", level=1, experience=30.0)
    print(f">({skill}, 2)")
    print(level_up_skill(skill, 2))

    # 9.5 Создание объекта data-класса на основе передаваемых параметров
    print("\n9.5. create_character")
    print(">(name='Mage', health=100, mana=200)")
    new_character = create_character(name='Mage', health=100, mana=200)
    print(new_character)


if __name__ == '__main__':
    main()
