"""
Language HTTP header parsing.
YOu received user's preferred languages in raw, not-parsed format. Server can accepts some restricted languages only,
described in server_acceptable_languages list. Write a function that would take user's preferred languages and
return list of languages that server can understand.
User may also send languages tags, not only entire language codes. If so, return all languages that matches with
given tag.
Order of languages must be preserved, duplicates are not allowed.
For example, if user input is "fr-AR, fr, pl=PL" and server accepts ["fr-FR", "fr-AR", "en-GB", "en-US"],
the output should be ['fr-AR', 'fr-FR'].
"fr-AR" must appear before "fr-FR", and "fr-AR" cannot be duplicated.
"""
from typing import List


def get_accepted_languages(user_language_header: str, server_acceptable_languages: List[str]) -> List[str]:
    parsed_user_langs = [lang.strip() for lang in user_language_header.split(",")]
    return [lang for lang in parsed_user_langs if lang in server_acceptable_languages]


def get_accepted_languages_with_tags(user_language_header: str, server_acceptable_languages: List[str]) -> List[str]:
    parsed_user_langs = [lang.strip() for lang in user_language_header.split(",")]
    already_added, accepted_langs = set(), []

    for lang in parsed_user_langs:
        if "-" not in lang:
            for server_lang in server_acceptable_languages:
                if server_lang.startswith(lang) and server_lang not in already_added:
                    accepted_langs.append(server_lang)
                    already_added.add(server_lang)
        elif lang in server_acceptable_languages and lang not in already_added:
            accepted_langs.append(lang)
            already_added.add(lang)

    return accepted_langs


if __name__ == '__main__':
    print(get_accepted_languages("fr-FR, en-US", ["fr-FR", "fr-AR", "en-GB", "en-US"]))
    print(get_accepted_languages("fr-FR, pl=PL", ["fr-FR", "fr-AR", "en-GB", "en-US"]))
    print(get_accepted_languages_with_tags("fr, pl=PL", ["fr-FR", "fr-AR", "en-GB", "en-US"]))
    print(get_accepted_languages_with_tags("fr-AR, fr, pl=PL", ["fr-FR", "fr-AR", "en-GB", "en-US"]))
