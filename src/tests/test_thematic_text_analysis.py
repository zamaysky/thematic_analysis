from schemas.thematic import BaseThemes, ThematicTextRequest, ThematicTextResponse
from client import Client


def test_base_themes(client: Client):
    response: BaseThemes = client.get_themes_list()
    assert response.themes


def test_send_text_for_analysis(client: Client):
    thematic_response1: ThematicTextResponse = client.send_text_for_analysis(
        ThematicTextRequest(text="кухня")
    )
    assert not thematic_response1.themes
    thematic_response2: ThematicTextResponse = client.send_text_for_analysis(
        ThematicTextRequest(text="тайская")
    )
    assert not thematic_response2.themes
    thematic_response3: ThematicTextResponse = client.send_text_for_analysis(
        ThematicTextRequest(text="кухня любые слова тайская любые слова")
    )
    assert len(thematic_response3.themes) == 2
