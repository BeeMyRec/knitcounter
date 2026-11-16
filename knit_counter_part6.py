# === Stage 6: Связанная сущность ===
# Project: KnitCounter
import os
import json
import uuid


class Session:
    def __init__(self, name, project_id):
        self.id = uuid.uuid4().hex
        self.name = name
        self.project_id = project_id
        self.count = 0


class SessionsStore:
    def __init__(self):
        self._sessions = {}
        self._path = os.path.join(os.path.dirname(__file__), 'sessions.json')

    def add(self, name, project_id):
        session = Session(name, project_id)
        self._sessions[session.id] = session
        self._save()
        return session

    def get(self, session_id):
        return self._sessions.get(session_id)

    def _save(self):
        data = {
            'sessions': [
                {'id': s.id, 'name': s.name, 'project_id': s.project_id, 'count': s.count}
                for s in self._sessions.values()
            ]
        }
        with open(self._path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
