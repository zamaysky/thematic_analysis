from typing import NoReturn

from more_itertools import first_true

from dal.thematic_dal import ThematicDal
from schemas.thematic_schemas import BaseThemes, ThematicTextResponse, ThematicTextRequest, ThemeResponseItem
from utils.text_utils import words_counter


class ThematicHandler:
    def __init__(self, thematic_dal: ThematicDal) -> NoReturn:
        self._thematic_dal = thematic_dal

    async def get_base_themes(self) -> BaseThemes:
        return await self._thematic_dal.get_theme_phrases()

    async def get_themes_by_text(self, text_request: ThematicTextRequest) -> ThematicTextResponse:
        theme_phrases: BaseThemes = await self._thematic_dal.get_theme_phrases(text_request.text)
        result = ThematicTextResponse(text=text_request.text)
        text_words = words_counter(text_request.text)
        for theme in theme_phrases:
            matched_phrase = first_true(
                theme,
                pred=lambda phrase: words_counter(phrase) <= text_words
            )
            if matched_phrase:
                result.themes.append(
                    ThemeResponseItem(
                        title=theme.title,
                        matched_phrase=matched_phrase,
                    )
                )
        return result

