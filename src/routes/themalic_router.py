from typing import Annotated

from fastapi import APIRouter, Body, Depends

from depends.thematic_depends import get_thematic_handler
from handlers.thematic_handlers import ThematicHandler
from schemas.thematic_schemas import ThematicTextRequest, BaseThemes, ThematicTextResponse

router = APIRouter(
    prefix=r'/v1/thematic',
    tags=['thematic']
)


@router.post(
    r'/text',
    summary='send text to thematic analysis',
    response_model=ThematicTextResponse
)
async def send_text_for_analysis(
        text_request: Annotated[ThematicTextRequest, Body],
        thematic_handler: Annotated[ThematicHandler, Depends(get_thematic_handler)]
) -> ThematicTextResponse:
    return await thematic_handler.get_themes_by_text(text_request)


@router.get(
    r'/themes',
    response_model=BaseThemes,
    summary='get base themes',
)
async def get_themes(
        thematic_handler: Annotated[ThematicHandler, Depends(get_thematic_handler)]
) -> BaseThemes:
    return await thematic_handler.get_base_themes()
