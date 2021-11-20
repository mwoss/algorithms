"""
Language HTTP header parsing.

"""
from typing import List, Set


def get_accepted_languages(user_language_header: str, server_acceptable_languages: Set[str]) -> List[str]:
    parsed_user_langs = [lang.strip() for lang in user_language_header.split(",")]
    return [lang for lang in parsed_user_langs if lang in server_acceptable_languages]
