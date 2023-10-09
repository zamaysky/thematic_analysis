import json
from functools import cache

from schemas.thematic import BaseThemes


@cache
def get_base_themes() -> BaseThemes:
    with open(r'./base_theme_phrases.json') as file:
        themes = json.load(file)
    return BaseThemes(
        themes=themes
    )
