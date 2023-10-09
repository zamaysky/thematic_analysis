from typing import Any, Counter, Iterator

from pydantic import BaseModel
from functools import cached_property

from utils.text_utils import words_counter


class BaseThemePhrases(BaseModel):
    title: str
    phrases: list[str]

    @cached_property
    def phrases_words_counters(self) -> list[Counter[str]]:
        return [
            words_counter(phrase)
            for phrase in self.phrases
        ]


class BaseThemes(BaseModel):
    themes: list[BaseThemePhrases]

    def __iter__(self) -> Iterator[BaseThemePhrases]:
        return iter(self.themes)


class ThematicTextRequest(BaseModel):
    text: str


class ThematicTextResponse(BaseModel):
    text: str
    themes: list[str] = []
