# === Stage 7: Связи между сущностями ===
# Project: KnitCounter
session_repository.py

from datetime import datetime

from project_repository import ProjectRepository


class SessionIntegrityError(Exception):
    pass


class SessionRepository:
    def __init__(self):
        self._sessions = {}

    def add(self, project, session):
        key = project['id']
        if key not in self._sessions:
            self._sessions[key] = []
        self._sessions[key].append(session)

    def get_all(self, project):
        if 'id' not in project:
            raise SessionIntegrityError('project missing id')
        sessions = self._sessions.get(project['id'], [])
        self._check_integrity(project, sessions)
        return list(sessions)

    def _check_integrity(self, project, sessions):
        for session in sessions:
            if 'project_id' not in session:
                raise SessionIntegrityError('session missing project_id')
            if session['project_id'] != project['id']:
                raise SessionIntegrityError('session project_id mismatch')
            if 'rows_done' not in session:
                raise SessionIntegrityError('session missing rows_done')
            if not isinstance(session['rows_done'], int):
                raise SessionIntegrityError('rows_done not integer')


class ProjectSessionBuilder:
    def __init__(self, project_repository=None, session_repository=None):
        self._project_repository = project_repository or ProjectRepository()
        self._session_repository = session_repository or SessionRepository()

    def build(self, project):
        project = self._project_repository.get(project['name'])
        return self._session_repository.get_all(project)
