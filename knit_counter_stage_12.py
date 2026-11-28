# === Stage 12: Поиск по нескольким словам ===
# Project: KnitCounter
def search_projects(query, projects):
    terms = parse_query(query)
    results = []
    for project in projects:
        name = project.get("name", "")
        item = project.get("item", "")
        yarn = project.get("yarn", "")
        rows = project.get("rows", "")
        text = " ".join(str(v).lower() for v in (name, item, yarn, rows))
        if matches(text, terms):
            results.append(project)
    return results


def parse_query(query):
    terms = []
    current = []
    for token in query.split():
        if token.startswith("-"):
            if current:
                terms.append(" ".join(current).strip().lower())
                current = []
        else:
            current.append(token.lower())
    if current:
        terms.append(" ".join(current).strip().lower())
    return terms


def matches(text, terms):
    text_terms = set(text.split())
    required = [t for t in terms if t != ""]
    excluded = [t for t in terms if t != ""]
    if not required and not excluded:
        return True
    for term in required:
        if term not in text_terms:
            return False
    for term in excluded:
        if term in text_terms:
            return False
    return True


if __name__ == "__main__":
    sample_projects = [
        {"name": "Зимний шарф", "item": "шарф", "yarn": "шерсть", "rows": 60},
        {"name": "Вязаная шапка", "item": "шапка", "yarn": "акрил", "rows": 40},
        {"name": "Спортивный свитер", "item": "свитер", "yarn": "хлопок", "rows": 120},
        {"name": "Летний платок", "item": "платок", "yarn": "лён", "rows": 30},
    ]

    print("Поиск: зимний")
    for p in search_projects("зимний", sample_projects):
        print(p["name"])

    print("\nПоиск: шапка -акрил")
    for p in search_projects("шапка -акрил", sample_projects):
        print(p["name"])

    print("\nПоиск: свитер платок")
    for p in search_projects("свитер платок", sample_projects):
        print(p["name"])

    print("\nПоиск: (без ключевых слов)")
    for p in search_projects("", sample_projects):
        print(p["name"])

    print("\nПоиск: только акрил (исключение)")
    for p in search_projects("акрил -акрил", sample_projects):
        print(p["name"])
