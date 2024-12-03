"""
Модуль main.py: запуск функций для демонстрации работы банковской системы.
Функция main вызывает функции из файла exceptions.py.
"""


from exceptions import (
    check_balance,
    validate_account_number,
    process_transaction,
    process_transaction_with_finally,
    validate_transfer_amount,
    validate_client_info,
    check_account_status,
    perform_transaction,
    close_account,
    register_client,
    check_service_availability,
    calculate_interest,
    NotEnoughFundsError,
    InactiveAccountError,
    AccountNotFoundError
)


# Функция, запускающая остальные
def main():
    """
    Основная функция для вызова всех функций.
    Выполняет тестирование каждой функции и обрабатывает исключения, 
    которые они могут выбрасывать.
    """

    # 1. Функции (2), выбрасывающие исключения
    try:
        print("Тест check_balance")
        print(">(1000, 500)")
        check_balance(1000, 500)
        print(">(1000, 1500)")
        check_balance(1000, 1500)
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")

    try:
        print("\nТест validate_account_number")
        print(">(123456)")
        validate_account_number(123456)
        print(">(\"abc123\")")
        validate_account_number("abc123")
    except ValueError as te:
        print(f"Ошибка типа: {te}")

    # 2. Функция с обработчиком исключения (без finally)
    print("\nТест process_transaction")
    print(">(1000, 500)")
    print(process_transaction(1000, 500))
    print(">(1000, 1500)")
    print(process_transaction(1000, 1500))

    # 3. Функция с обработчиком исключения (с finally)
    print("\nТест process_transaction_with_finally")
    print(">(1000, 500)")
    print(process_transaction_with_finally(1000, 500))
    print(">(1000, 2000)")
    print(process_transaction_with_finally(1000, 2000))

    # 4. Функции (3), обрабатывающие 3 и более типов исключений
    print("\nТест validate_transfer_amount")
    print(">(100)")
    validate_transfer_amount(100)
    print(">(-100)")
    validate_transfer_amount(-100)

    print("\nТест validate_client_info")
    print(">(\"Иван\", 25)")
    validate_client_info("Иван", 25)
    print(">(\"\", 25)")
    validate_client_info("", 25)
    print(">(\"Кто-тоСОченьДлиннымИменем\", 30)")
    validate_client_info("Кто-тоСОченьДлиннымИменем", 30)
    print(">(\"Анна\", 17)")
    validate_client_info("Анна", 17)

    account_data = {
        12345: "active",
        67890: "inactive",
        54321: "blocked"
    }

    print("\nТест check_account_status")
    print(f"account_data: {account_data}")
    print(">(account_data, 12345)")
    check_account_status(account_data, 12345)
    print(">(account_data, 11111)")
    check_account_status(account_data, 11111)
    print(">(account_data, 67890)")
    check_account_status(account_data, 67890)
    print(">([], 12345)")
    check_account_status([], 12345)

    # 5. Функция, генерирующая и обрабатывающая исключения
    print("\nТест perform_transaction")
    account_data = {
        12345: ("active", 500.0),
        67890: ("inactive", 300.0),
        54321: ("active", 100.0)
    }
    print(f"new account_data: {account_data}")
    print(">(account_data, 12345, 50) >> account_data")
    account_data = perform_transaction(account_data, 12345, 50)
    print(">(account_data, 67890, 50) >> account_data")
    account_data = perform_transaction(account_data, 67890, 50)
    print(">(account_data, 12345, -10) >> account_data")
    account_data = perform_transaction(account_data, 12345, -10)
    #perform_transaction(account_data, 54321, 200)
    #perform_transaction(account_data, 11111, 50)
    #perform_transaction([], 12345, 50)
    print(f"account_data: {account_data}")

    # 6. Пользовательские исключения - в файле exceptions.py

    # 7. Функция выбрасывает и обрабатывает пользовательское исключение
    print("\nТест close_account")
    print(">(account_data, 12345) >> account_data")
    account_data = close_account(account_data, 12345)
    print(">(account_data, 12345) >> account_data")
    account_data = close_account(account_data, 12345)
    print(">(account_data, 67890) >> account_data")
    account_data = close_account(account_data, 67890)
    print(f"account_data: {account_data}")

    client_data = {
        1: {"name": "Иван", "accounts": []}
    }

    # 8. Функции (3) с разной логикой, демонстрирующие работу исключений
    print("\nТест register_client")
    print(f"client_data: {client_data}")
    print(">(client_data, 2, \"Всеволод\") >> client_data")
    client_data = register_client(client_data, 2, "Всеволод")
    try:
        print(">(client_data, 1, \"Иван\") >> client_data")
        client_data = register_client(client_data, 1, "Иван")
    except ValueError as e:
        print(f"Ошибка: {e}")
    try:
        print(">(client_data, 3, \"\") >> client_data")
        client_data = register_client(client_data, 3, "")
    except AccountNotFoundError as e:
        print(f"Ошибка: {e}")
    print(f"client_data: {client_data}")

    client_data[1]["accounts"].append("savings")
    print("\nДобавлю активный счёт клиенту")
    print(f"client_data: {client_data}")

    print("\nТест check_service_availability")
    print(">(client_data, 1, \"credit\")")
    check_service_availability(client_data, 1, "credit")
    try:
        print(">(client_data, 1, \"insurance\")")
        check_service_availability(client_data, 1, "insurance")
    except NotImplementedError as e:
        print(f"Ошибка: {e}")
    try:
        print(">(client_data, 2, \"credit\")")
        check_service_availability(client_data, 2, "credit")
    except InactiveAccountError as e:
        print(f"Ошибка: {e}")

    print("\nТест calculate_interest")
    print(">(1000, 5, 12)")
    calculate_interest(1000, 5, 12)
    print(">(2000, 3, 6)")
    calculate_interest(2000, 3, 6)
    try:
        print(">(1000, -5, 12)")
        calculate_interest(1000, -5, 12)
    except ValueError as e:
        print(f"Ошибка: {e}")
    try:
        print(">(0, 5, 12)")
        calculate_interest(0, 5, 12)
    except NotEnoughFundsError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
