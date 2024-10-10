# CRUD-REST-API

CRUD REST API для работы с книгами, созданное с использованием FastAPI, Sqlite, Sqlalchemy, Docker.

> [!NOTE]
> Помимо стандартной реализации CRUD, Update наделен возможностью изменения отдельных полей книги.

> [!CAUTION]
> Реализована простая валидация данных:
> - Строки проверяются на размер,
> - Автор проверяется на корректность имени,
> - Год публикации должен быть корректным, не превышать текущий год.

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone git@github.com:Molodchina/CRUD-REST-API.git
   cd CRUD-REST-API
   docker-compose up --build
   ```
2. Откройте браузер по [адресу](http://127.0.0.1:8000/docs)

## Использование

1. ![Swagger Main Screen](./docs/main_screen.png?raw=true)

2. ![Swagger Post Screen](./docs/post.png?raw=true)

3. ![Swagger Get ALL Screen](./docs/get_all.png?raw=true)

4. ![Swagger Get Screen](./docs/get.png?raw=true)

5. ![Swagger Update Screen](./docs/update.png?raw=true)

6. ![Swagger Delete Screen](./docs/delete.png?raw=true)

## Project-Tree
```
CRUD-REST-API/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── requirements.txt
│   └── schemas.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```