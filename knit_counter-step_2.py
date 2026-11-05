# === Stage 2: Проверка полей ===
# Project: KnitCounter
import re


def normalize_stitch_count(value):
    """Нормализует числовое поле: строку в целое число."""
    if value is None:
        raise ValueError("Поле не может быть пустым")
    number = re.search(r"-?\d+", str(value).strip())
    if not number:
        raise ValueError("Не удалось распознать число")
    return int(number.group())


def normalize_name(value):
    """Нормализует строковые поля: убирает пробелы по краям."""
    if value is None:
        raise ValueError("Поле не может быть пустым")
    return str(value).strip()


def validate_project(project):
    """Проверяет все поля сущности проекта и возвращает список ошибок."""
    errors = []

    if not project.get("name"):
        errors.append("Укажите название проекта")

    if not project.get("item"):
        errors.append("Укажите, что вы вяжете")

    yarn = project.get("yarn")
    if not yarn:
        errors.append("Укажите используемую пряжу")

    rows = project.get("rows")
    if not rows:
        errors.append("Укажите количество рядов")

    if "rows" in project and project["rows"] is not None:
        try:
            rows_value = normalize_stitch_count(project["rows"])
            if rows_value <= 0:
                errors.append("Количество рядов должно быть больше нуля")
            else:
                project["rows"] = rows_value
        except ValueError as error:
            errors.append(str(error))

    if "name" in project and project["name"] is not None:
        project["name"] = normalize_name(project["name"])

    if "item" in project and project["item"] is not None:
        project["item"] = normalize_name(project["item"])

    if "yarn" in project and project["yarn"] is not None:
        project["yarn"] = normalize_name(project["yarn"])

    return errors


if __name__ == "__main__":
    sample = {
        "name": "  Свитер  ",
        "item": "Свитер",
        "yarn": "  шерсть  ",
        "rows": "  42  ",
    }

    errors = validate_project(sample)
    if errors:
        print("Найдены ошибки:")
        for error in errors:
            print(" -", error)
    else:
        print("Проект валиден")
        print("Название:", sample["name"])
        print("Изделие:", sample["item"])
        print("Пряжа:", sample["yarn"])
        print("Рядов:", sample["rows"])
