import asyncio
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dal.thematic_dal import ThematicDal
from depends.thematic_depends import get_es
from schemas.thematic_schemas import BaseThemes, ThemePhrase


async def main():
    dal = ThematicDal(get_es())
    with open(r'./base_theme_phrases.json') as file:
        themes = json.load(file)
    base_themes = BaseThemes(
        themes=themes
    )
    for theme in base_themes:
        for phrase in theme:
            await dal.index_theme_phrase(ThemePhrase(
                title=theme.title,
                phrase=phrase
            ))


if __name__ == '__main__':
    asyncio.run(main())
