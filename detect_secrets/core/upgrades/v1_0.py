import os
from typing import Any
from typing import cast
from typing import Dict
from typing import Iterable

from ...exceptions import InvalidFile
from ..plugins.util import get_plugins_from_file


def upgrade(baseline: Dict[str, Any]) -> None:
    for function in [
        _migrate_filters,
        _rename_high_entropy_string_arguments,
        _migrate_custom_plugins,
    ]:
        function(baseline)


def _migrate_filters(baseline: Dict[str, Any]) -> None:
    """
    In v1.0.0, we introduced the idea of `filters`. This consolidated a variety of different
    false positive filters into a configurable layout. To reduce upgrade friction, this will
    contain the default filters used before this version upgrade.
    """
    pass


def _rename_high_entropy_string_arguments(baseline: Dict[str, Any]) -> None:
    """
    During the great refactor for v1.0.0, we also decided to rename these arguments for
    consistency and simplicity.
    """
    pass

    # TODO: KeywordDetector?


def _migrate_custom_plugins(baseline: Dict[str, Any]) -> None:
    pass
