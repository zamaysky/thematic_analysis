from typing import Any, Counter, Iterator

from pydantic import BaseModel, Field
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
    text: str = Field(min_length=1, max_length=5000)


class ThematicTextResponse(ThematicTextRequest):
    themes: list[str] = []
