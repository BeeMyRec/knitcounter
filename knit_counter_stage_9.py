# === Stage 9: Фильтрация записей ===
# Project: KnitCounter
from datetime import datetime, date


def filter_projects_by_item(projects, item):
    return [project for project in projects if project["item"] == item]


def filter_projects_by_date_range(projects, start_date, end_date):
    start_date = parse_date(start_date)
    end_date = parse_date(end_date)
    result = []
    for project in projects:
        created = parse_date(project["created"])
        if start_date is None or created >= start_date:
            if end_date is None or created <= end_date:
                result.append(project)
    return result


def parse_date(value):
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def filter_projects(projects, item=None, start_date=None, end_date=None):
    result = projects
    if item is not None:
        result = filter_projects_by_item(result, item)
    if start_date is not None or end_date is not None:
        result = filter_projects_by_date_range(result, start_date, end_date)
    return result
