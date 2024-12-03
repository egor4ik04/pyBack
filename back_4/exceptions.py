"""
exceptions.py
Модуль с функциями для демонстрации работы исключений в банковской системе.
"""

# 1. Функции (2), выбрасывающие исключения
def check_balance(balance, amount):
    """
    Проверяет, достаточно ли средств для снятия.
    Выбрасывает ValueError, если средств недостаточно.
    """
    if amount > balance:
        raise ValueError("Недостаточно средств на счёте.")


def validate_account_number(account_number):
    """
    Проверяет корректность номера счёта.
    Выбрасывает ValueError, если номер некорректен.
    """
    if not isinstance(account_number, (int, float)) or len(str(account_number)) != 6:
        raise ValueError("Номер счёта должен состоять из 6 цифр.")


# 2. Функция с обработчиком исключения (без finally)
def process_transaction(balance, amount):
    """
    Пытается провести транзакцию, снимая средства с баланса.
    Выбрасывает ValueError, если средств недостаточно.
    Обрабатывает исключение с выводом сообщения.
    Возвращает итоговый баланс и успешность транзакции.
    """
    try:
        check_balance(balance, amount)
        balance -= amount
        print(f"Транзакция прошла успешно. Баланс: {balance}")
        return balance, True
    except ValueError as e:
        print(f"Ошибка: {e}")


# 3. Функция с обработчиком исключения (с finally)
def process_transaction_with_finally(balance, amount):
    """
    Пытается провести транзакцию, снимая средства с баланса.
    Выбрасывает ValueError, если средств недостаточно.
    Обрабатывает исключение с выводом сообщения.
    Блок finally гарантирует нормальное завершение работы функции.
    Возвращает итоговый баланс и успешность транзакции.
    """
    success = False
    new_balance = balance
    try:
        check_balance(balance, amount)
        new_balance -= amount
        print(f"Транзакция прошла успешно. Баланс: {new_balance}")
        success = True
    except ValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершаем операцию. Пожалуйста, проверьте свой баланс.")
    return new_balance, success


# 4. Функции (3), обрабатывающие 3 и более типов исключений
def validate_transfer_amount(amount):
    """
    Проверяет корректность суммы перевода.
    Обрабатывает ValueError, TypeError, и OverflowError.
    """
    try:
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом.")
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной.")
        if amount > 1e6:
            raise OverflowError("Сумма перевода превышает допустимый лимит.")
        print(f"Сумма {amount} проверена успешно.")
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except OverflowError as e:
        print(f"Ошибка переполнения: {e}")
    finally:
        print("Проверка суммы перевода завершена.")


def validate_client_info(name, age):
    """
    Проверяет данные клиента.
    Обрабатывает ValueError, TypeError, и IndexError.
    """
    try:
        if not isinstance(name, str) or not name.strip():
            raise TypeError("Имя должно быть непустой строкой.")
        if not isinstance(age, int) or age < 18:
            raise ValueError("Возраст должен быть целым числом не менее 18.")
        if len(name) > 20:
            raise IndexError("Имя превышает допустимую длину.")
        print(f"Данные клиента {name}, {age} проверены успешно.")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except IndexError as e:
        print(f"Ошибка длины: {e}")
    finally:
        print("Проверка данных клиента завершена.")


def check_account_status(account_data, account_number):
    """
    Проверяет статус счёта.
    Обрабатывает KeyError, ValueError, и TypeError.
    """
    try:
        if not isinstance(account_data, dict):
            raise TypeError("Данные о счёте должны быть словарём.")
        if account_number not in account_data:
            raise KeyError("Счёт с указанным номером не найден.")
        if account_data[account_number] != "active":
            raise ValueError("Счёт неактивен или заблокирован.")
        print(f"Счёт {account_number} активен и доступен для операций.")
    except KeyError as e:
        print(f"Ошибка ключа: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    finally:
        print("Проверка статуса счёта завершена.")


# 5. Функция, генерирующая и обрабатывающая исключения
def perform_transaction(account_data, account_number, amount):
    """
    Выполняет транзакцию, проверяя наличие счёта,
    статус счёта и корректность суммы перевода.
    Генерирует исключения ValueError, KeyError, и TypeError.
    Обрабатывает все сгенерированные исключения.
    finally завершает операцию.
    Возвращает изменённые данные account_data.
    """
    try:
        if not isinstance(account_data, dict):
            raise TypeError("Данные счёта должны быть словарём.")
        if account_number not in account_data:
            raise KeyError("Указанный счёт не найден.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма должна быть положительным числом.")

        account_status, balance = account_data[account_number]
        if account_status != "active":
            raise ValueError("Счёт заблокирован или неактивен.")
        check_balance(balance, amount)

        account_data[account_number] = (account_status, balance - amount)
        print(f"Транзакция успешно завершена. Остаток: {balance - amount}")

    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except KeyError as e:
        print(f"Ошибка ключа: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    finally:
        print("Операция завершена. Проверьте данные счёта.")

    return account_data


# 6. Пользовательские исключения (3)
class NotEnoughFundsError(Exception):
    """
    Исключение для недостатка средств на счёте.
    """

    def __init__(self, message="Недостаточно средств для выполнения операции."):
        super().__init__(message)


class AccountNotFoundError(Exception):
    """
    Исключение для отсутствия указанного счёта.
    """

    def __init__(self, message="Счёт с указанным номером не найден."):
        super().__init__(message)


class InactiveAccountError(Exception):
    """
    Исключение для неактивного или заблокированного счёта.
    """

    def __init__(self, message="Счёт заблокирован или неактивен."):
        super().__init__(message)


# 7. Функция выбрасывает пользовательское исключение
def close_account(account_data, account_number):
    """
    Закрывает банковский счёт. Errors:
        AccountNotFoundError для отсутствия счёта.
        InactiveAccountError для уже закрытого счёта.
    Возвращает изменнные данные и сообщает об успешном закрытии.
    """
    try:
        if account_number not in account_data:
            raise AccountNotFoundError()

        status, _ = account_data[account_number]
        if status != "active":
            raise InactiveAccountError()

        account_data[account_number] = ("closed", 0)
        print(f"Счёт {account_number} успешно закрыт.")

    except (AccountNotFoundError, InactiveAccountError, ValueError) as e:
        print(f"Ошибка: {e}")

    finally:
        print("Проверка завершена.")

    return account_data


# 8. Функции (3) с разной логикой, демонстрирующие работу исключений
def register_client(client_data, client_id, name):
    """
    Регистрирует нового клиента. Errors:
        ValueError, если клиент уже существует.
        AccountNotFoundError, если неверные данные клиента.
    """
    if client_id in client_data:
        raise ValueError("Клиент с таким ID уже существует.")
    if not name:
        raise AccountNotFoundError("Имя клиента не может быть пустым.")
    client_data[client_id] = {"name": name, "accounts": []}
    print(f"Клиент {name} успешно зарегистрирован.")
    return client_data


def check_service_availability(client_data, client_id, service_name):
    """
    Проверяет доступность услуги для клиента. Errors:
        KeyError, если клиента не существует.
        NotImplementedError, если услуга недоступна.
        InactiveAccountError, если счёт клиента не активен.
    """
    if client_id not in client_data:
        raise KeyError("Клиент не найден.")
    available_services = ["credit", "investment"]
    if service_name not in available_services:
        raise NotImplementedError("Услуга временно недоступна.")
    if len(client_data[client_id]["accounts"]) == 0:
        raise InactiveAccountError("У клиента нет активных счетов.")
    print(f"Услуга {service_name} доступна для клиента {client_id}.")


def calculate_interest(balance, rate, months):
    """
    Рассчитывает проценты по вкладу и возвращает значение. Errors:
        ValueError, если данные некорректны.
        NotEnoughFundsError, если недостаточно средств на балансе.
    """
    if balance < 0 or rate < 0 or months < 1:
        raise ValueError("Некорректные данные для расчёта.")
    if balance == 0:
        raise NotEnoughFundsError("Недостаточно средств для расчёта.")
    interest = round(balance * (rate / 100) * (months / 12), 2)
    print(f"Начисленные проценты: {interest}")
    return interest
