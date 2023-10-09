from typing import Annotated

from fastapi import APIRouter, Body, Depends

from depends.thematic_depends import get_base_themes
from handlers.thematic_handlers import get_text_themes
from schemas.thematic import ThematicTextRequest, BaseThemes, ThematicTextResponse

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
        base_themes: Annotated[BaseThemes, Depends(get_base_themes)]
) -> ThematicTextResponse:
    return get_text_themes(
        text=text_request.text,
        themes=base_themes
    )


@router.get(
    r'/themes',
    summary='get base themes',
    response_model=BaseThemes
)
async def get_themes(
    base_themes: Annotated[BaseThemes, Depends(get_base_themes)]
) -> BaseThemes:
    return base_themes
