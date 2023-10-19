"""CSV-file parser"""

INPUT_FILENAME = "Corp_Summary.csv"
OUTPUT_FILENAME = "report.csv"


def _execute_report_one(all_data: dict):
    """
    Execute only report 1.

    :param all_data: Dict with all information
        from the input file, result of the `read_file` function
    :return:
        None
    """

    team_info = {}
    for department, division in zip(
        all_data["Департамент"], all_data["Отдел"]
    ):
        if team_info.get(department) is None:
            team_info[department] = []

        if division not in team_info[department]:
            team_info[department].append(division)

    for team in team_info:
        print(f"{team}:")
        print("\n".join(
            [f"\t{team}" for team in team_info[team]]
        ))


def _get_department_info(all_data: dict) -> dict:
    """
    Get department info dict.

    :param all_data: Dict with all information
        from the input file, result of the `read_file` function
    :return:
        Dict with salaries.
        Structure:
            dict[DEPARTMENT_NAME] = [SALARY1, SALARY2, ...]
    """
    department_info = {}
    for department, salary in zip(
        all_data["Департамент"], all_data["Оклад"]
    ):
        if department_info.get(department) is None:
            department_info[department] = []

        department_info[department].append(salary)

    return department_info


def _get_text_report_two(department_info: dict) -> str:
    """
    Get text information for the second report.

    :param department_info: dict with salaries, result of
        `_get_department_info` function.
    :return:
        Report text.
    """
    report_text = []
    for department, salaries in department_info.items():
        length = len(salaries)
        min_salary = min(salaries)
        mean_salary = sum(salaries) / length
        max_salary = max(salaries)

        department_info[department] = (
            length, f"{min_salary} - {max_salary}", mean_salary
        )

        _report_text = (
            f"{department}:\n"
            f"\tЧисленность: {length}\n"
            f"\tЗарплатная вилка: {min_salary} - {max_salary}\n"
            f"\tСредняя зарплата: {mean_salary}"
        )
        report_text.append(_report_text)

    report_text = "\n".join(report_text)
    return report_text


def execute_report(all_data: dict, report_num: int) -> None:
    """
    Execute one of the report scripts.

    :param all_data: Dict with all information
        from the input file, result of the `read_file` function
    :param report_num: one of the 1, 2, 3
    :return:
        None
    """
    if report_num not in [1, 2, 3]:
        raise ValueError("Unexpected report number. Should be out of 3.")

    if report_num == 1:
        _execute_report_one(all_data)
        return

    department_info = _get_department_info(all_data)
    report_text = _get_text_report_two(department_info)

    if report_num == 2:
        print(report_text)

    elif report_num == 3:
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as file:
            file.write("Департамент,Численность,Зарплатная вилка,Средняя зарплата\n")
            for department, (length, fork, salary) in department_info.items():
                file.write(f"{department},{length},{fork},{salary}\n")
        print(f"Report saved as {OUTPUT_FILENAME}.")


def parse_line(line: str, columns: list[str]) -> dict:
    """
    Parse line from input file via split function.

    :param line: current line from the input file
    :param columns: columns of data in the input file
    :return:
        Dict with information from this line.
        Structure:
            data[COLUMN_NAME] = COLUMN_VALUE
    """
    if columns is None:
        raise ValueError

    data = {}
    for col, value in zip(columns, line.strip().split(";")):
        if col == "Оценка":
            value = float(value)
        elif col == "Оклад":
            value = int(value)

        data[col] = value

    return data


def read_file() -> dict:
    """
    Read input file.

    :return:
        Dict with all information from the inout file.
        Structure:
            dict[COLUMN_NAME] = [ALL_COLUMN_VALUES]
    """
    with open(INPUT_FILENAME, "r", encoding="utf-8") as file:
        columns = file.readline().strip().split(";")

        all_data = {col: [] for col in columns}

        for line in file.readlines():
            data = parse_line(line, columns=columns)

            for col in columns:
                all_data[col].append(data[col])

    return all_data


def parse_file() -> None:
    """
    Read file and run report function.

    :return:
        None
    """
    all_data = read_file()

    print("Введите опцию получаемого отчета:\n"
          "\t1. Иерархия команд.\n"
          "\t2. Сводный отчет по департаментам.\n"
          "\t3. Выгруженный отчет по департаментам в csv-файле.\n")

    execute_report(all_data, report_num=int(input()))


if __name__ == "__main__":
    parse_file()
