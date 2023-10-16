from functools import cached_property
from typing import Counter, Iterator

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass

from utils.text_utils import eval_words_counter


class BaseThemePhrases(BaseModel):
    title: str
    phrases: list[str]

    @cached_property
    def phrases_words_counters(self) -> dict[str, Counter[str]]:
        return {
            phrase: eval_words_counter(phrase)
            for phrase in self
        }

    def __iter__(self) -> Iterator[str]:
        return iter(self.phrases)


@dataclass(frozen=True)
class ThemePhrase:
    title: str
    phrase: str
    words_counter: Counter[str]

    def __hash__(self):
        return hash((self.title, self.phrase))


class BaseThemes(BaseModel):
    themes: list[BaseThemePhrases]

    def __iter__(self) -> Iterator[BaseThemePhrases]:
        return iter(self.themes)

    @cached_property
    def reversed_index(self) -> dict[str, set[ThemePhrase]]:
        index = {}
        for theme in self.themes:
            for phrase, words_counter in theme.phrases_words_counters.items():
                for word in words_counter:
                    index.setdefault(
                        word,
                        set()
                    ).add(
                        ThemePhrase(
                            title=theme.title,
                            phrase=phrase,
                            words_counter=words_counter
                        )
                    )
        return index


class ThematicTextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=5000)


class ThematicTextResponse(ThematicTextRequest):
    themes: list[str] = []
