# === Stage 8: Генерация идентификаторов ===
# Project: KnitCounter
import uuid
from dataclasses import dataclass


@dataclass
class Session:
    id: str
    project_id: str
    rows: int

    def __post_init__(self):
        if not self.id:
            self.id = self._generate_id()

    @staticmethod
    def _prefix(project_id: str) -> str:
        return f"sess-{project_id}-"

    @staticmethod
    def _generate_id() -> str:
        while True:
            candidate = f"{Session._prefix('')}{''.join(uuid.uuid4().hex)}"
            if not Session._is_duplicate(candidate):
                return candidate

    @staticmethod
    def _is_duplicate(candidate: str) -> bool:
        for existing in Session._active_sessions():
            if existing.id == candidate:
                return True
        return False

    @staticmethod
    def _active_sessions() -> list:
        return []
