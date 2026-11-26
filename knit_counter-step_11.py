# === Stage 11: Текстовый поиск ===
# Project: KnitCounter
import re


def normalize(text):
    return text.casefold()


def highlight_matches(text, pattern):
    if not text or not pattern:
        return text
    normalized_text = normalize(text)
    normalized_pattern = normalize(pattern)
    if normalized_pattern not in normalized_text:
        return text
    regex = re.compile(
        re.escape(normalized_pattern),
        re.IGNORECASE,
    )
    def _replace(match):
        return '\033[7;31m' + match.group(0) + '\033[0m'
    return regex.sub(_replace, text)


def build_search_filter(pattern):
    def filter_projects(projects):
        pattern = normalize(pattern)
        if not pattern:
            return list(projects)
        normalized = [normalize(p) for p in projects]
        matches = [p for p, n in zip(projects, normalized) if pattern in n]
        return matches
    return filter_projects
