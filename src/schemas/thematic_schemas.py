from typing import Iterator

from pydantic import BaseModel, Field


class BaseThemePhrases(BaseModel):
    title: str
    phrases: list[str]

    def __iter__(self) -> Iterator[str]:
        return iter(self.phrases)


class BaseThemes(BaseModel):
    themes: list[BaseThemePhrases]

    def __iter__(self) -> Iterator[BaseThemePhrases]:
        return iter(self.themes)


class ThemePhrase(BaseModel):
    title: str
    phrase: str


class ThematicTextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=5000)


class ThemeResponseItem(BaseModel):
    title: str
    matched_phrase: str


class ThematicTextResponse(ThematicTextRequest):
    themes: list[ThemeResponseItem] = []
