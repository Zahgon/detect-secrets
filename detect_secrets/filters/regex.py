import re
from functools import lru_cache
from typing import List
from typing import Pattern

from ..settings import get_settings
from .util import get_caller_path


def should_exclude_line(line: str) -> bool:
    pass


@lru_cache(maxsize=1)
def _get_line_exclusion_regex() -> List[Pattern]:
    pass


def should_exclude_file(filename: str) -> bool:
    pass


@lru_cache(maxsize=1)
def _get_file_exclusion_regex() -> List[Pattern]:
    pass


def should_exclude_secret(secret: str) -> bool:
    pass


@lru_cache(maxsize=1)
def _get_secret_exclusion_regex() -> List[Pattern]:
    pass
