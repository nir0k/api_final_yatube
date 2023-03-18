# api_final

## Описание. 

Социальная сеть для писателей, желающих поделиться своим оригинальнным контентом. 
Возможности:
- Размещение постов
- Группы
- Комментарии
- Подписка
- Авторизация
- RestAPI

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git
```

```
cd kittygram2plus
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# Примеры API

[Доступ к нолному описанию API] (http://127.0.0.1:8000/redoc/)

- Получение JWT-tokena:
http://127.0.0.1:8000/api/v1/jwt/create/

Playload:
```JSON
{
"username": "string",
"password": "string"
}
```
- Получение публикаций:
http://127.0.0.1:8000/api/v1/posts/

- Получение публикаций с фильтрацией:
http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4

limit - количесвто публикаций
offset - с какой публикации начать выдачу

- Получение одного поста:
http://127.0.0.1:8000/api/v1/posts/{ID}/

- Создание публикации:
http://127.0.0.1:8000/api/v1/posts/
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены
 ```JSON
{
"text": "string",
"image": "string",
"group": 0
}
 ```

- Получение списка групп:
Получение списка доступных сообществ.
http://127.0.0.1:8000/api/v1/groups/

- Получение подписок
Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/follow/

- Поиск подписки
http://127.0.0.1:8000/api/v1/follow/?search="{username}"
