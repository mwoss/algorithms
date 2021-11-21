"""
Language HTTP header parsing.

"""
from typing import List, Set


def get_accepted_languages(user_language_header: str, server_acceptable_languages: Set[str]) -> List[str]:
    parsed_user_langs = [lang.strip() for lang in user_language_header.split(",")]
    return [lang for lang in parsed_user_langs if lang in server_acceptable_languages]


# client: [fr, fr-FR, en-US]    server: [fr-FR, fr-AR, en-US, en-GB]
def get_accepted_languages_with_tags(user_language_header: str, server_acceptable_languages: Set[str]) -> List[str]:
    parsed_user_langs = [lang.strip() for lang in user_language_header.split(",")]
    accepted_langs = set([])
    for lang in parsed_user_langs:
        if "-" not in lang:
            for server_lang in server_acceptable_languages:
                if server_lang.startswith(lang):
                    accepted_langs.add(server_lang)
        elif lang in server_acceptable_languages:
            accepted_langs.add(lang)
    return list(accepted_langs)
