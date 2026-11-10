# === Stage 3: Хранилище в памяти ===
# Project: KnitCounter
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class KnitProject:
    id: int
    name: str
    item: str
    yarn: str
    rows: int

    def add_row(self) -> None:
        self.rows += 1


@dataclass
class ProjectStore:
    projects: Dict[str, KnitProject] = field(default_factory=dict)
    _counter: int = 0

    def add(self, name: str, item: str, yarn: str, rows: int = 0) -> KnitProject:
        self._counter += 1
        project = KnitProject(
            id=self._counter,
            name=name,
            item=item,
            yarn=yarn,
            rows=rows,
        )
        self.projects[str(project.id)] = project
        return project

    def get(self, project_id: int) -> KnitProject | None:
        return self.projects.get(str(project_id))

    def list(self) -> List[KnitProject]:
        return list(self.projects.values())

    def remove(self, project_id: int) -> bool:
        return self.projects.pop(str(project_id), None) is not None
