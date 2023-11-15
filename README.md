# Первоначальные настройки
Создать .env файл в корневой директории проекта с содержимым
```
POSTGRES_DB = example_db
POSTGRES_USER = example_user
POSTGRES_PASSWORD = example_password
RABBITMQ_DEFAULT_USER = example_rabbit_user
RABBITMQ_DEFAULT_PASS = example_rabbit_password
TOKEN = example_token_for_external_service
```
Данные из примера нужно заменить на свои
# Запуск приложения
С помощью консоли перейти в корневую директорию и выполнить
```
docker-compose up
```
