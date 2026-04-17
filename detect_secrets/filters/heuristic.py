import os
import re
import string
from functools import lru_cache
from typing import Optional
from typing import Pattern

from detect_secrets.plugins.base import BasePlugin
from detect_secrets.plugins.base import RegexBasedDetector


def is_sequential_string(secret: str) -> bool:
    pass


def is_potential_uuid(secret: str) -> bool:
    pass


@lru_cache(maxsize=1)
def _get_uuid_regex() -> Pattern:
    pass


def is_likely_id_string(secret: str, line: str, plugin: Optional[BasePlugin] = None) -> bool:
    pass


@lru_cache(maxsize=1)
def _get_id_detector_regex() -> Pattern:
    """
    Regex Details:
    ^(id|myid|userid) -> Common id identifiers with no prefix
    _id               -> id identifier with prefixes allowed
    s?                -> Optional plural id identifier
    [^a-z0-9]         -> Non-letter/numeric character
    """
    pass


def is_non_text_file(filename: str) -> bool:
    pass


# We don't scan files with these extensions.
# Note: We might be able to do this better with
#       `subprocess.check_output(['file', filename])`
#       and look for "ASCII text", but that might be more expensive.
#
#       Definitely something to look into, if this list gets unruly long.
IGNORED_FILE_EXTENSIONS = set(
    (
        '.7z',
        '.bin',
        '.bmp',
        '.bz2',
        '.class',
        '.css',
        '.dmg',
        '.doc',
        '.eot',
        '.exe',
        '.gif',
        '.gz',
        '.ico',
        '.iml',
        '.ipr',
        '.iws',
        '.jar',
        '.jpg',
        '.jpeg',
        '.lock',
        '.map',
        '.mo',
        '.pdf',
        '.png',
        '.prefs',
        '.psd',
        '.rar',
        '.realm',
        '.s7z',
        '.sum',
        '.svg',
        '.tar',
        '.tif',
        '.tiff',
        '.ttf',
        '.webp',
        '.woff',
        '.xls',
        '.xlsx',
        '.zip',
    ),
)


def is_templated_secret(secret: str) -> bool:
    """
    Filters secrets that are shaped like: {secret}, <secret>, or ${secret}.
    """
    pass


def is_prefixed_with_dollar_sign(secret: str) -> bool:
    # NOTE: This is broken out into its own function since it has more chance of increasing
    # false negatives than `is_templated_secret` (e.g. secrets that actually start with a $).
    # This is best used with files that actually use this as a means of referencing variables.
    # TODO: More intelligent filetype handling?
    pass


def is_indirect_reference(line: str) -> bool:
    """
    Filters secrets that take the form of:

        secret = get_secret_key()

    or

        secret = request.headers['apikey']
    """
    pass


@lru_cache(maxsize=1)
def _get_indirect_reference_regex() -> Pattern:
    # Regex details:
    #   ([^\v=!:]*)     ->  Something before the assignment or comparison
    #   \s*             ->  Some optional whitespaces
    #   (:=?|[!=]{1,3}) ->  Assignment or comparison: :=, =, ==, ===, !=, !==
    #   \s*             ->  Some optional whitespaces
    #   (
    #       [\w.-]+     ->  Some alphanumeric character, dot or -
    #       [\[\(]      ->  Start of indirect reference: [ or (
    #       [^\v]*      ->  Something except line breaks
    #       [\]\)]      ->  End of indirect reference: ] or )
    #   )
    pass


def is_lock_file(filename: str) -> bool:
    pass


def is_not_alphanumeric_string(secret: str) -> bool:
    """
    This assumes that secrets should have at least ONE letter in them.
    This helps avoid clear false positives, like `*****`.
    """
    pass


def is_swagger_file(filename: str) -> bool:
    """
    Filters swagger files and paths, like swagger-ui.html or /swagger/.
    """
    pass


@lru_cache(maxsize=1)
def _get_swagger_regex() -> Pattern:
    pass
