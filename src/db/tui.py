from .backend.memory import create_employee, select_employees


def _read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Ошибка: введите целое число.")


def _read_optional_int(prompt: str) -> int | None:
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return None
        try:
            return int(raw)
        except ValueError:
            print("Ошибка: введите целое число или оставьте поле пустым.")


def _read_nonempty_string(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: значение не может быть пустым.")


def _print_employees(employee_list: list) -> None:
    if not employee_list:
        print("Сотрудники не найдены.")
        return
    print(f"{'ID'} | {'Имя'} | {'Должность'} | {'Зарплата'} | {'Отдел'}")
    print("-" * 65)
    for e in employee_list:
        print(f"{e[0]} | {e[1]} | {e[2]} | {e[3]} | {e[4]}")


def _add_employee() -> None:
    print("\n--- Добавление сотрудника ---")
    employee_id = _read_int("ID сотрудника: ")
    name = _read_nonempty_string("Имя: ")
    position = _read_nonempty_string("Должность: ")
    salary = _read_int("Зарплата: ")
    department = input("Отдел: ").strip()
    try:
        _print_employees([create_employee(employee_id, name, position, salary, department)])
    except ValueError as e:
        print(f"Ошибка: {e}")


def _find_employees() -> None:
    print("\n--- Поиск сотрудников ---")
    print("Введите критерии поиска (пустое поле = пропустить фильтр):")
    employee_id = _read_optional_int("ID сотрудника: ")
    name = input("Имя: ").strip() or None
    position = input("Должность: ").strip() or None
    salary = _read_optional_int("Зарплата: ")
    department = input("Отдел: ").strip() or None
    _print_employees(select_employees(employee_id, name, position, salary, department))


def run() -> None:
    actions = {
        "1": _add_employee,
        "2": _find_employees,
        "3": lambda: _print_employees(select_employees()),
    }
    while True:
        print("\n=== База данных 'Сотрудники' (in-memory) ===")
        print("1. Добавить сотрудника")
        print("2. Найти сотрудников")
        print("3. Показать всех сотрудников")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == "0":
            print("Выход из программы.")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Неверный ввод. Повторите.")
