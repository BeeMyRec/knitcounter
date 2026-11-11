# === Stage 4: Редактирование записей ===
# Project: KnitCounter
import re


ALLOWED_PROJECT_FIELDS = {
    "title": str,
    "garment": str,
    "yarn": str,
    "row_count": int,
}

ROW_COUNT_MIN = 1
ROW_COUNT_MAX = 100000


def _is_blank(value):
    return isinstance(value, str) and value.strip() == ""


def _validate_row_count(value):
    if not isinstance(value, int) or isinstance(value, bool):
        return False
    return ROW_COUNT_MIN <= value <= ROW_COUNT_MAX


def _coerce_row_count(value):
    return int(value)


def validate_project_patch(patch):
    if not isinstance(patch, dict):
        raise ValueError("patch должен быть словарём")

    unknown = set(patch.keys()) - set(ALLOWED_PROJECT_FIELDS.keys())
    if unknown:
        raise ValueError("недопустимые поля: " + ", ".join(sorted(unknown)))

    cleaned = {}
    for field, raw in patch.items():
        expected_type = ALLOWED_PROJECT_FIELDS[field]
        if field == "row_count":
            if not isinstance(raw, str) and not isinstance(raw, int) or isinstance(raw, bool):
                raise ValueError("поле row_count должно быть числом")
            if not _validate_row_count(_coerce_row_count(raw)):
                raise ValueError(
                    "row_count должно быть целым от "
                    + str(ROW_COUNT_MIN)
                    + " до "
                    + str(ROW_COUNT_MAX)
                )
            cleaned[field] = _coerce_row_count(raw)
        elif expected_type is str:
            text = raw if isinstance(raw, str) else str(raw)
            if _is_blank(text):
                raise ValueError("поле " + field + " не может быть пустым")
            cleaned[field] = text
        else:
            raise ValueError("неподдерживаемое поле: " + field)

    return cleaned


def apply_project_patch(project, patch):
    cleaned = validate_project_patch(patch)
    merged = dict(project)
    merged.update(cleaned)
    return merged
