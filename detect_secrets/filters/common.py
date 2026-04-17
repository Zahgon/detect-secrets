import os
from functools import lru_cache
from typing import cast

import requests

from ..constants import VerifiedResult
from ..core.plugins import Plugin
from ..settings import get_settings
from ..util.code_snippet import CodeSnippet
from ..util.inject import call_function_with_arguments
from .util import get_caller_path


def is_invalid_file(filename: str) -> bool:
    pass


def is_baseline_file(filename: str) -> bool:
    pass


@lru_cache(maxsize=1)
def _get_baseline_filename() -> str:
    pass


def is_ignored_due_to_verification_policies(
    secret: str,
    plugin: Plugin,
    context: CodeSnippet,
) -> bool:
    """
    Valid policies include:
        - Only VERIFIED_TRUE
        - Can be UNVERIFIED or VERIFIED_TRUE
        - Disabled check.

    There's no such thing as "only verified false", because if you're going to verify
    something, and it's verified false, why are you still including it as a valid secret?
    """
    pass


@lru_cache(maxsize=1)
def _get_verification_policy() -> VerifiedResult:
    pass
