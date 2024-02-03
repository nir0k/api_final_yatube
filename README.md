# api_final_yatube

## Choose Your Language

- [English](README.md)
- [Русский](README.ru.md)

---

## Description

Backend server for a social network for writers wishing to share their original content. REST API features include:

- **Posts:** Create, edit, update, and delete.
- **Comments:** Fetch, update, and delete.
- **Groups:** Participation and management.
- **Followings:** Follow users.
- **Authorization:** JWT authorization support.

## Installation

1. **Clone the repository:**
    ```sh
    git clone git@github.com:nir0k/api_final_yatube.git
    cd api_final_yatube
    ```
2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```
3. **Install dependencies:**
    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. **Apply migrations:**
    ```sh
    cd yatube_api
    python3 manage.py migrate
    ```
5. **Start the project:**
    ```sh
    python3 manage.py runserver
    ```

## API Examples

- **Obtaining JWT Token:** `POST http://127.0.0.1:8000/api/v1/jwt/create/`

    Payload:
    ```json
    {
    "username": "string",
    "password": "string"
    }
    ```
- **Fetching posts**: GET http://127.0.0.1:8000/api/v1/posts/

- **Filtering posts**: GET http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4
    - `limit` - number of posts to fetch.
    - `offset` - which post to start from.

- Fetching a single post: GET http://127.0.0.1:8000/api/v1/posts/{ID}/

- Creating a post: POST http://127.0.0.1:8000/api/v1/posts/

    Anonymous requests are not allowed.
    ```json
    {
    "text": "string",
    "image": "string",
    "group": 0
    }
    ```

- **Fetching a list of groups**: GET http://127.0.0.1:8000/api/v1/groups/

- **Fetching followings**: GET http://127.0.0.1:8000/api/v1/follow/

    Returns all followings of the user making the request. Anonymous requests are not allowed.

- **Searching for a following**: GET http://127.0.0.1:8000/api/v1/follow/?search="{username}"

**Full API Description** : http://127.0.0.1:8000/redoc/