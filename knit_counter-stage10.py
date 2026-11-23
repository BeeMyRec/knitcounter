# === Stage 10: Сортировка записей ===
# Project: KnitCounter
import json
from datetime import datetime


def _parse_date(value):
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
    return datetime.min


def sort_projects(projects, key="name", reverse=False):
    if not isinstance(projects, list):
        return projects

    if key == "created_at":
        def sort_key(item):
            return _parse_date(item.get("created_at"))
    elif key == "name":
        def sort_key(item):
            return str(item.get("name", "")).lower()
    else:
        def sort_key(item):
            return item.get(key)

    return sorted(projects, key=sort_key, reverse=reverse)


def sort_by_name(projects, reverse=False):
    return sort_projects(projects, key="name", reverse=reverse)


def sort_by_created_at(projects, reverse=False):
    return sort_projects(projects, key="created_at", reverse=reverse)


def load_projects(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_projects(path, projects):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(projects, fh, ensure_ascii=False, indent=2)


def main():
    path = "projects.json"
    projects = load_projects(path)

    projects = sort_by_name(projects)

    for project in projects:
        print(project["name"], project["created_at"])

    save_projects(path, projects)


if __name__ == "__main__":
    main()
