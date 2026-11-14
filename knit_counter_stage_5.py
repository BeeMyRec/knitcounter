# === Stage 5: Удаление и восстановление ===
# Project: KnitCounter
import datetime
import threading
from collections import defaultdict


class KnitProject:
    """Сущность «проект» со статусом удаления (мягкое удаление)."""

    ACTIVE = "active"
    SOFT_DELETED = "soft_deleted"

    def __init__(self, name, product, yarn, row_count):
        self.id = str(datetime.datetime.now().timestamp())
        self.name = name
        self.product = product
        self.yarn = yarn
        self.row_count = row_count
        self.deleted = False
        self.deleted_at = None
        self.deleted_reason = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "product": self.product,
            "yarn": self.yarn,
            "row_count": self.row_count,
            "deleted": self.deleted,
            "deleted_at": self.deleted_at,
            "deleted_reason": self.deleted_reason,
        }

    def soft_delete(self, reason="user requested"):
        self.deleted = True
        self.deleted_at = datetime.datetime.now().isoformat()
        self.deleted_reason = reason
        return self

    def restore(self):
        self.deleted = False
        self.deleted_at = None
        self.deleted_reason = None
        return self


class KnitStore:
    """Хранилище проектов с поддержкой мягкого удаления и восстановления."""

    def __init__(self):
        self._lock = threading.Lock()
        self._projects = {}

    def add(self, project):
        with self._lock:
            self._projects[project.id] = project
        return project

    def get(self, project_id):
        with self._lock:
            project = self._projects.get(project_id)
            return project

    def list_active(self):
        with self._lock:
            return [p for p in self._projects.values() if not p.deleted]

    def list_soft_deleted(self):
        with self._lock:
            return [p for p in self._projects.values() if p.deleted]

    def delete(self, project_id, reason="user requested"):
        with self._lock:
            project = self._projects.get(project_id)
            if project is None:
                return None
            project.soft_delete(reason=reason)
            return project

    def restore(self, project_id):
        with self._lock:
            project = self._projects.get(project_id)
            if project is None or not project.deleted:
                return None
            project.restore()
            return project

    def permanently_remove(self, project_id):
        with self._lock:
            return self._projects.pop(project_id, None)


def example_usage():
    store = KnitStore()
    project = KnitProject("Мой свитер", "Свитер", "Хлопок", 120)
    store.add(project)
    store.delete(project.id, reason="на паузе")
    store.restore(project.id)
    print(project.to_dict())
