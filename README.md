# API для Yatube

## Описание

**Yatube** — социальная сеть для публикации личных дневников. Этот проект — её REST API:
через него можно публиковать записи, читать ленту, комментировать публикации,
просматривать сообщества и подписываться на других авторов.

API позволяет подключить к Yatube любые клиенты: мобильное приложение, бота
или отдельный фронтенд.

Возможности:

* публикации — просмотр всех записей, создание, редактирование и удаление своих;
* комментарии к публикациям;
* сообщества (группы) — только просмотр;
* подписки на авторов с поиском по подпискам;
* аутентификация по JWT-токенам.

Неаутентифицированные пользователи могут только читать данные (кроме подписок —
они доступны только аутентифицированным). Изменять и удалять контент может
только его автор.

## Технологии

* Python 3.9+
* Django 3.2
* Django REST Framework 3.12
* Simple JWT

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/Digital-Bogila/api_yatube.git
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Для Windows:

```bash
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```bash
cd yatube_api
python3 manage.py migrate
```

Создать суперпользователя (пользователи через API не регистрируются):

```bash
python3 manage.py createsuperuser
```

Запустить проект:

```bash
python3 manage.py runserver
```

Полная документация API будет доступна по адресу http://127.0.0.1:8000/redoc/

## Примеры запросов

### Получение JWT-токена

`POST /api/v1/jwt/create/`

```json
{
    "username": "string",
    "password": "string"
}
```

Ответ:

```json
{
    "refresh": "string",
    "access": "string"
}
```

Токен передаётся в заголовке запроса: `Authorization: Bearer <access>`.

### Получение публикаций с пагинацией

`GET /api/v1/posts/?limit=2&offset=4`

```json
{
    "count": 123,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=6",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2",
    "results": [
        {
            "id": 5,
            "author": "anton",
            "text": "Текст публикации",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": null,
            "group": 1
        }
    ]
}
```

Без параметров `limit` и `offset` возвращается полный список публикаций.

### Создание публикации

`POST /api/v1/posts/`

```json
{
    "text": "Текст публикации",
    "group": 1
}
```

Ответ:

```json
{
    "id": 14,
    "author": "anton",
    "text": "Текст публикации",
    "pub_date": "2021-10-14T20:41:29.648Z",
    "image": null,
    "group": 1
}
```

### Добавление комментария

`POST /api/v1/posts/14/comments/`

```json
{
    "text": "Отличный пост!"
}
```

Ответ:

```json
{
    "id": 4,
    "author": "anton",
    "text": "Отличный пост!",
    "created": "2021-10-14T20:45:11.388Z",
    "post": 14
}
```

### Подписка на автора

`POST /api/v1/follow/`

```json
{
    "following": "leo"
}
```

Ответ:

```json
{
    "user": "anton",
    "following": "leo"
}
```

Поиск по подпискам: `GET /api/v1/follow/?search=leo`

## Автор

[Digital-Bogila](https://github.com/Digital-Bogila)
