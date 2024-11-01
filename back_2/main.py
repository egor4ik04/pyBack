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
    print("\nДемонстрация функций:")
    demo_funcs()


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
    print("a =", a)
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

    a = 0b101
    print(f"a = 0b{a:0b} ({a})")
    a &= 0b011 #0b001
    print(f"Присваивание с логическим и (a &= 0b011 ({0b011})): 0b{a:0b} ({a})")
    a |= 0b010 #0b011
    print(f"Присваивание с логическим или (a |= 0b010 ({0b010})): 0b{a:0b} ({a})")
    a ^= 0b110 #0b101
    print(f"Присваивание с логическим xor (a ^= 0b110 ({0b110})): 0b{a:0b} ({a})")

    a = 16
    print(f"a = {a} (0b{a:0b})")
    a >>= 2
    print(f"Присваивание со сдвигом (a >>= 2): {a} (0b{a:0b})")
    a <<= 1
    print(f"Присваивание со сдвигом (a <<= 1): {a} (0b{a:0b})")


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


def demo_funcs():
    '''Демонстрация работы с функциями'''

    def func_basic():
        """Простая функция без параметров и возвращаемого значения."""
        print("Это простая функция")

    def func_with_parameters(a, b=5):
        """Функция с позиционными и именованными параметрами, где второй параметр по умолчанию."""
        print(f"Параметры: a={a}, b={b}")
        return a + b

    def func_with_variable_args(*args, **kwargs):
        """Функция с произвольным числом позиционных и именованных аргументов."""
        print("Позиционные аргументы:", args)
        print("Именованные аргументы:", kwargs)
        return sum(args) + sum(kwargs.values())

    def func_with_special_params(x, y, /, z, *, w=10):
        """Функция с обязательными позиционными и именованными параметрами.

        x и y должны быть переданы по позиции.
        z уникален.
        w является именованным параметром с значением по умолчанию.
        """
        return (x + y + z) * w

    # Вызов функций и вывод результатов
    func_basic()
    print("Результат func_with_parameters(3, 4):", func_with_parameters(3, 4))
    print("Результат func_with_parameters(3):", func_with_parameters(3))
    print("Результат func_with_variable_args(1, 2, 3, x=4, y=5):",
          func_with_variable_args(1, 2, 3, x=4, y=5))
    print("Результат function_with_special_params(1, 2, 3, w=4):",
          func_with_special_params(1, 2, 3, w=4))
    print("Результат function_with_special_params(1, 2, w=4, z=3):",
          func_with_special_params(1, 2, w=4, z=3))

main()
