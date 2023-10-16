from collections import Counter

from schemas.thematic import BaseThemes, ThematicTextResponse, ThemePhrase
from utils.text_utils import eval_words_counter


def get_text_themes(
        text: str,
        themes: BaseThemes
) -> ThematicTextResponse:
    words: Counter[str] = eval_words_counter(text)
    text_themes = set()
    for word in words:
        themes_phrases: set[ThemePhrase] | None = themes.reversed_index.get(word, set())
        for theme_phrase in themes_phrases:
            if theme_phrase.title not in text_themes and theme_phrase.words_counter <= words:
                text_themes.add(theme_phrase.title)

    return ThematicTextResponse(
        text=text,
        themes=text_themes
    )
