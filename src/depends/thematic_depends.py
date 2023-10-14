from functools import cache
from typing import Annotated

from elasticsearch import AsyncElasticsearch
from fastapi import Depends

from config import settings
from dal.thematic_dal import ThematicDal
from handlers.thematic_handlers import ThematicHandler


def get_es() -> AsyncElasticsearch:
    return AsyncElasticsearch(settings.elastic_uri)


def get_thematic_dal(
        es: Annotated[AsyncElasticsearch, Depends(get_es)]
) -> ThematicDal:
    return ThematicDal(es)


@cache
def get_thematic_handler(
        thematic_dal: Annotated[ThematicDal, Depends(get_thematic_dal)]
) -> ThematicHandler:
    return ThematicHandler(thematic_dal)
