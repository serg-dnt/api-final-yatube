# Yatube API

REST API для проекта Yatube — социальной сети для публикации постов, комментариев, подписок и сообществ.

---

## О проекте

API позволяет:

- Создавать, просматривать, редактировать и удалять посты
- Комментировать посты
- Создавать и просматривать сообщества (группы)
- Подписываться на пользователей
- Аутентификация с помощью JWT токенов
- Пагинация с помощью LimitOffsetPagination

---

## Технологии

- Python 3.12+
- Django 5.x
- Django REST Framework
- Djoser (для регистрации и JWT аутентификации)
- SimpleJWT (JWT токены)
- SQLite

---

## Установка и запуск

1. Клонируйте репозиторий

```bash

git clone <репозиторий>
cd <папка_проекта>
```

2. Создайте и активируйте виртуальное окружение

```bash

python -m venv venv
source venv/bin/activate # Linux/macOS
venv/Scripts/activate    # Windows
```

3. Установите зависимости

```bash

pip install -r requirements.txt
```

4. Примените миграции

```bash

python manage.py migrate
```

5. Запустите сервер
```bash

python manage.py runserver
```
 
## Документация

Документация к API доступна по адресу:
```bash

/redoc/
```