type EmployeeRecord = tuple[int, str, str, int, str]

Employees: list[EmployeeRecord] = []


def _employee_exists(employee_id: int) -> bool:
    return any(record[0] == employee_id for record in Employees)


def create_employee(
        employee_id: int,
        name: str,
        position: str,
        salary: int,
        department: str,
) -> EmployeeRecord:
    if employee_id < 0:
        raise ValueError("ID должен быть неотрицательным числом.")
    if _employee_exists(employee_id):
        raise ValueError(f"Сотрудник с ID = {employee_id} уже существует.")
    if not name.strip():
        raise ValueError("Имя сотрудника не может быть пустым.")
    if not position.strip():
        raise ValueError("Должность не может быть пустой.")
    if salary < 0:
        raise ValueError("Зарплата не может быть отрицательной.")

    record: EmployeeRecord = (
        employee_id,
        name.strip(),
        position.strip(),
        salary,
        department.strip(),
    )
    Employees.append(record)
    return record


def select_employees(
        employee_id: int | None = None,
        name: str | None = None,
        position: str | None = None,
        salary: int | None = None,
        department: str | None = None,
) -> list[EmployeeRecord]:
    if (employee_id is None and name is None and position is None
            and salary is None and department is None):
        return Employees.copy()

    return [
        r for r in Employees
        if (employee_id is None or r[0] == employee_id)
           and (name is None or r[1] == name)
           and (position is None or r[2] == position)
           and (salary is None or r[3] == salary)
           and (department is None or r[4] == department)
    ]
