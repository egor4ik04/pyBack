'''
    Получение навыков работы с операторами преобразования и присваивания, 
    условными операторами, операторами цикла, переменными, функциями
'''

def main():
    """Основная функция, вызывающая демонстрации по разделам."""
    print("Демонстрация переменных:")
    demo_variables()
    print("\nДемонстрация преобразования типов:")
    demo_type_casting()
    print("\nДемонстрация операторов присваивания:")
    demo_assignment_operators()
    print("\nДемонстрация условных операторов:")
    demo_conditional_operators()
    print("\nДемонстрация циклов:")
    demo_cycles()


def demo_variables():
    """Демонстрация создания и использования переменных различных типов."""
    # Числовые типы данных
    integer_num = 42
    float_num = 3.1415
    complex_num = 2 + 3j
    scientific_num = 1.5e2  # Экспоненциальная запись (150)
    binary_num = 0b1010  # Двоичное представление (10)
    octal_num = 0o52  # Восьмеричное представление (42)
    hex_num = 0x2A  # Шестнадцатеричное представление (42)

    # Логический тип данных
    bool_true = True
    bool_false = False

    # Строковый тип данных
    name = "Alice"
    multiline_str = """Это
многострочная
строка"""

    print("Числовые переменные:", integer_num, float_num, complex_num,
          scientific_num, binary_num, octal_num, hex_num)
    print("Логические переменные:", bool_true, bool_false)
    print("Строки:", name, multiline_str)


def demo_type_casting():
    """Демонстрация операторов преобразования типов."""
    str_num = "123"
    float_num = 3.56
    bool_val = False

    print("Преобразование строки в число:", int(str_num))
    print("Преобразование числа в строку:", str(float_num))
    print("Преобразование bool в строку:", str(bool_val))
    print("Преобразование числа в bool:", bool(0), bool(42))
    # False для 0, True для любого ненулевого числа
    print("Преобразование строки в bool:", bool(""), bool("Hello"))
    # False для пустой строки, True для непустой


def demo_assignment_operators():
    """Демонстрация операторов присваивания."""
    a = 5
    print("Изначально a =", a)
    a += 3
    print("Присваивание с увеличением (a += 3):", a)
    a -= 2
    print("Присваивание с уменьшением (a -= 2):", a)
    a *= 4
    print("Присваивание с умножением (a *= 4):", a)
    a /= 2
    print("Присваивание с делением (a /= 2):", a)
    a //= 3
    print("Присваивание с целочисленным делением (a //= 3):", a)
    a %= 5
    print("Присваивание с остатком (a %= 5):", a)
    a **= 2
    print("Присваивание с возведением в степень (a **= 2):", a)


def demo_conditional_operators():
    """Демонстрация условных операторов."""
    age = int(input("Введите любой возраст, например - 20: "))
    name = input("Введите любое имя, например - Alice: ")

    if age >= 18:
        print("Совершеннолетний")
    else:
        print("Несовершеннолетний")

    # Использование логических операторов
    if age >= 18 and name == "Alice":
        print("Совершеннолетний по имени Alice")
    elif age >= 18 or name == "Alice":
        print("Либо совершеннолетний, либо имя Alice")
    else:
        print("Несовершеннолетний и не Alice")

    # Тернарный оператор
    result = "Совершеннолетний" if age >= 18 else "Несовершеннолетний"
    print("Результат тернарного оператора:", result)


def demo_cycles():
    """Демонстрация операторов цикла."""
    print("Цикл for с range:")
    for i in range(3):
        print("Итерация", i)

    print("\nЦикл for по списку:")
    fruits = ["яблоко", "банан", "вишня"]
    for fruit in fruits:
        print("Фрукт:", fruit)

    print("\nЦикл while:")
    count = 0
    while count < 3:
        print("Итерация", count)
        count += 1

    print("\nЦикл с break и continue:")
    for i in range(5):
        if i == 2:
            continue
        if i == 4:
            break
        print("Итерация", i)


main()
