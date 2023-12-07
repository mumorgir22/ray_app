# ray_app

Проект ray_app - предоставляет пользователям возможность осуществлять CRUD операции (Создание, Чтение, Обновление, Удаление) с записями в базе данных. Стэк - Fastapi, Postgres, Alembic, SqlAlchemy, Poetry, Redis, Docker-compose, JWT. Weather API - погода по городам юзеров, фоновое обновление

## Установка и Запуск

1. Клонирование репозитория:

```bash
git clone https://github.com/mumorgir22/ray_app.git
```
2. Директория проекта:
```bash
cd ray_app/
```
3. Сборка и запуск докеров:
```bash
docker compose build
```
```bash
docker compose up -d
```
4. Запуска приложения фастапи:
```bash
uvicorn main:app --reload
```
5. #### Веб-приложение будет доступно по адресу http://127.0.0.1:8000/docs

## CRUD

   Регистрация пользователя (POST запрос) http://127.0.0.1:8000/auth/signup/
   
```python
# Через body
{
    "username": "user",
    "email": "test@mail.com",
    "password": "pass",
    "city": "SPB"
}
```
```python
# Output
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDIxMjgxNDQsImlhdCI6MTcwMTk1NTM0NCwic2NvcGUiOiJhY2Nlc3NfdG9rZW4iLCJ1c2VyX2lkIjoyNH0.KZ3CUD2R_1k9gtl3g6WowRZWTvPMRXLDtQ1BUlDUoSU",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDM2ODMzNDQsImlhdCI6MTcwMTk1NTM0NCwic2NvcGUiOiJyZWZyZXNoX3Rva2VuIiwidXNlcl9pZCI6MjR9.X_n_oAVhiIO-UKSa6qcwaEw4UGxNXlQ0Em2RQ__4I40"
}
```
   Логин пользователя (POST запрос) http://127.0.0.1:8000/auth/login/
   
```python
# Через body
{
    "email": "test@mail.com",
    "password": "pass"
}
```
```python
# Output
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDIxMjgxNDQsImlhdCI6MTcwMTk1NTM0NCwic2NvcGUiOiJhY2Nlc3NfdG9rZW4iLCJ1c2VyX2lkIjoyNH0.KZ3CUD2R_1k9gtl3g6WowRZWTvPMRXLDtQ1BUlDUoSU",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDM2ODMzNDQsImlhdCI6MTcwMTk1NTM0NCwic2NvcGUiOiJyZWZyZXNoX3Rva2VuIiwidXNlcl9pZCI6MjR9.X_n_oAVhiIO-UKSa6qcwaEw4UGxNXlQ0Em2RQ__4I40"
}
```
Получение информации о пользователе (GET запрос) http://127.0.0.1:8000/users/user/

```python
# Output
{
    "username": "test_user",
    "email": "test@mail.com",
    "phone": null,
    "city": "SPB",
    "weather": {
        "temperature": "-16.04",
        "wind_speed": "3"
    }
}
```

   Создание блога (POST запрос) http://127.0.0.1:8000/blogs/
```python
# Через body
{
    "name": "some_name",
    "description": "some_description",
    "image": "some_image"
}
```
Так же реализовано:

обновление блога - (PATCH запрос) http://127.0.0.1:8000/blogs/{blog_id}
```python
# Через body
{
    "name": str | None,
    "description": str | None,
    "image": str | None,
}
```


удаление (DELETE запрос) http://127.0.0.1:8000/blogs/{blog_id}

Блоги пользователя (GET запрос) http://127.0.0.1:8000/blogs/


```python
# Output
[
    {
        "id": 8,
        "name": "dwdd",
        "description": "dwqdwq",
        "image": null
    },
    {
        "id": 9,
        "name": "blog_name",
        "description": "blog_description",
        "image": "blog_image"
    }
]
```
## Тестирование
Для тестирования добавлены скрипты:

Регистрация пользователя
```bash
python3 tests/scripts/users/signup.py
```
Логин пользователя
```bash
python3 tests/scripts/users/login.py
```
Получение данных о юзере
```bash
python3 tests/scripts/users/get_user.py
```
Создание блога
```bash
python3 tests/scripts/blogs/create_blog.py
```
Обновление блога
```bash
python3 tests/scripts/blogs/update_blog.py
```
Удаление блога
```bash
python3 tests/scripts/blogs/delete_blog.py
```
Получение всех блогов пользователя
```bash
python3 tests/scripts/blogs/get_blogs.py
```

