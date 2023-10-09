## Зависимости

Для запуска проекта на сервере необходимо установить [docker](https://docs.docker.com/engine/install/ubuntu/)

## Список сервисов

- python3.11.2 + fastapi
- NGINX 1.25.2

Запустить проект:

   ```bash
   docker compose up --detach --build
   ```

Документация:
```
http://localhost/docs
```

Запуск тестов
```bash
docker exec -it thematic_analysis_backend pytest
```

Пример запроса:
```bash
curl --location 'localhost/v1/thematic/text' \
--header 'Content-Type: application/json' \
--data '{
    "text": "кухня fdsadfadsdf тайская asdfads"
}'
```