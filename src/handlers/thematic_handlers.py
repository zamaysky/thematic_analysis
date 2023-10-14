from typing import NoReturn

from dal.thematic_dal import ThematicDal
from schemas.thematic_schemas import BaseThemes, ThematicTextResponse, ThematicTextRequest, BaseThemePhrases
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
            for phrase in theme:
                if words_counter(phrase) <= text_words:
                    result.themes.append(BaseThemePhrases(
                        title=theme.title,
                        phrases=[phrase]
                    ))
                    break
        return result

