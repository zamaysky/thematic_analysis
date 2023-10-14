from fastapi.testclient import TestClient
from httpx import Response
from starlette import status

from main import app
from schemas.thematic_schemas import BaseThemes, ThematicTextResponse, ThematicTextRequest


class Client:
    def __init__(self):
        self._client = TestClient(app)

    def get_themes_list(self) -> BaseThemes:
        response: Response = self._client.get(r'v1/thematic/themes')
        assert response.status_code == status.HTTP_200_OK
        return BaseThemes.model_validate_json(response.text)

    def send_text_for_analysis(self, text_request: ThematicTextRequest):
        response: Response = self._client.post(
            r'v1/thematic/text',
            data=text_request.model_dump_json()
        )
        assert response.status_code == status.HTTP_200_OK
        return ThematicTextResponse.model_validate_json(response.text)
