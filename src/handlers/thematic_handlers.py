from collections import Counter

from schemas.thematic import BaseThemes, ThematicTextResponse
from utils.text_utils import words_counter


def get_text_themes(
        text: str,
        themes: BaseThemes
) -> ThematicTextResponse:
    words: Counter[str] = words_counter(text)
    text_themes = [
        theme.title
        for theme in themes
        for phrase in theme.phrases_words_counters
        if phrase <= words

    ]
    return ThematicTextResponse(
        text=text,
        themes=text_themes
    )
