# === Stage 1: Каркас модуля ===
# Project: KnitCounter
knitcounter/project.py

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Project:
    title: str
    garment: str
    yarn: str
    rows: int = 0
    pattern: Optional[str] = None
    sessions: list = field(default_factory=list)

    def add_session(self, session):
        self.sessions.append(session)

    def set_rows(self, rows):
        self.rows = rows

    def display(self):
        print(f"Проект: {self.title}")
        print(f"  Изделие:  {self.garment}")
        print(f"  Пряжа:    {self.yarn}")
        print(f"  Рядов:    {self.rows}")
        if self.pattern:
            print(f"  Схема:    {self.pattern}")


def demo_projects():
    projects = [
        Project(
            title="Шарф 'Зимний'",
            garment="Шарф",
            yarn="Ангора",
            rows=120,
            pattern="Паттерн 1",
        ),
        Project(
            title="Свитер 'Тёплый'",
            garment="Свитер",
            yarn="Мериносовая шерсть",
            rows=240,
            pattern="Паттерн 3",
        ),
        Project(
            title="Митенки 'Весенние'",
            garment="Митенки",
            yarn="Хлопок",
            rows=60,
            pattern="Паттерн 2",
        ),
    ]
    return projects


def main():
    projects = demo_projects()
    print("Демо-проекты KnitCounter:")
    for index, project in enumerate(projects, start=1):
        print()
        project.display()
        print(f"  [Проект {index}]")


if __name__ == "__main__":
    main()
