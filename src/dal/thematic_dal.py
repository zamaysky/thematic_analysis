from typing import NoReturn

from elastic_transport import ObjectApiResponse
from elasticsearch import AsyncElasticsearch
from more_itertools import map_reduce

from schemas.thematic_schemas import ThemePhrase, BaseThemes, BaseThemePhrases


class ThematicDal:
    INDEX_NAME = 'themes'

    def __init__(self, es: AsyncElasticsearch) -> NoReturn:
        self._es = es

    async def index_theme_phrase(self, theme_phrase: ThemePhrase) -> NoReturn:
        await self._es.index(
            index=self.INDEX_NAME,
            body=theme_phrase.model_dump(),
        )

    async def get_theme_phrases(
            self,
            phrase: str | None = None
    ) -> BaseThemes:
        theme_phrases: ObjectApiResponse = await self._es.search(
            index=self.INDEX_NAME,
            body=self._build_phrase_search_body(phrase) if phrase else None
        )
        return BaseThemes(
            themes=[
                BaseThemePhrases(
                    title=title,
                    phrases=phrases
                )
                for title, phrases in map_reduce(
                    theme_phrases.body['hits']['hits'],
                    keyfunc=lambda x: x['_source']['title'],
                    valuefunc=lambda x: x['_source']['phrase']
                ).items()
            ]
        )

    @staticmethod
    def _build_phrase_search_body(phrase: str) -> dict[str, ...]:
        return {
            "query": {
                "match": {
                    "phrase": {
                        "query": phrase,
                        "operator": "or"
                    }
                }
            }
        }
