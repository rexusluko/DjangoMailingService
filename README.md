# Первоначальные настройки
Создать .env файл в корневой директории проекта с содержимым
```
POSTGRES_DB = example_db
POSTGRES_USER = example_user
POSTGRES_PASSWORD = example_password
RABBITMQ_DEFAULT_USER = example_rabbit_user
RABBITMQ_DEFAULT_PASS = example_rabbit_password
TOKEN = example_token_for_external service
```
Данные из примера нужно заменить на свои
# Запуск приложения
С помощью консоли перейти в корневую директорию и выполнить
```
docker-compose up
```
# Работа с приложением
OpenAPI документация находится на http://127.0.0.1:8000/docs/
# Дополнительные задания
3. Подготовлен docker-compose для запуска всех сервисов проекта одной командой
5. По адресу /docs/ открывается страница со Swagger UI и в нём отображается описание разработанного API
9. Каждое сообщение пытается отправиться максимум 10 секунд, если не получилось, то сообщение попробует отправиться с следущей итерацией