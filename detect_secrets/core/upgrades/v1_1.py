from typing import Any
from typing import Dict


def upgrade(baseline: Dict[str, Any]) -> None:
    for function in [
        _add_new_default_filters,
    ]:
        function(baseline)


def _add_new_default_filters(baseline: Dict[str, Any]) -> None:
    pass
