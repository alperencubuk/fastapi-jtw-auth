# FastAPI JWT Auth

### Summary:

FastAPI project with JWT Authentication.

---

### Endpoints Table:

| Request URL              | Description                                                               |  HTTP  |
| ------------------------ | ------------------------------------------------------------------------- |  ----  |
| /login                   | Login with username and password. Returns access_token and refresh_token. | `POST` |
| /refresh                 | Send refresh token on Authorization header and  get access token.         | `POST` |
| /register                | Create a new user.                                                        | `POST` |
| /me                      | Get authenticated user information.                                       | `GET`  |

---

### Requirements:
* Docker and Docker Compose

### How to Run:

```
docker-compose up --build
```

### Example Requests:

---

#### Request:
```http request
POST /register
```

#### Request Body:
```json
{
    "username": "alperen",
    "password": "123456",
    "email": "alperen@mail.com"
}
```

#### Response:
```json
{
    "id": 1,
    "created": "2022-11-13T17:47:51.428216",
    "updated": "2022-11-13T17:47:51.428223",
    "username": "alperen",
    "email": "alperen@mail.com"
}
```

---

#### Request:
```http request
POST /login
```

#### Request Body:
```json
{
    "username": "alperen",
    "password": "123456",
}
```

#### Response:
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0IiwiaWF0IjoxNjY4MzYxNjkwLCJuYmYiOjE2NjgzNjE2OTAsImp0aSI6ImU0MTAyYjVmLWViMzUtNGU1OS04MTAwLThmOGUyZTI5YjEyYyIsImV4cCI6MTY2ODM2NTI5MCwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZX0.fzE7dBM-LqlO3NZOozOO9dEEBH63O6ez8F2Cwm1pu9A",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0IiwiaWF0IjoxNjY4MzYxNjkwLCJuYmYiOjE2NjgzNjE2OTAsImp0aSI6ImE0Mjk3N2Q1LWNiY2MtNGNkNy1iZjVlLWJkZTE4ZDFiYTc0NyIsImV4cCI6MTY3MDk1MzY5MCwidHlwZSI6InJlZnJlc2gifQ.1RjcFR3gpOarts10bh2kn7uYKfITgt9o5y2zQA1FQy4",
    "token_type": "bearer"
}
```

---

#### Request:
```http request
POST /refresh
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0IiwiaWF0IjoxNjY4MzYxNjkwLCJuYmYiOjE2NjgzNjE2OTAsImp0aSI6ImE0Mjk3N2Q1LWNiY2MtNGNkNy1iZjVlLWJkZTE4ZDFiYTc0NyIsImV4cCI6MTY3MDk1MzY5MCwidHlwZSI6InJlZnJlc2gifQ.1RjcFR3gpOarts10bh2kn7uYKfITgt9o5y2zQA1FQy4
```

#### Response:
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0IiwiaWF0IjoxNjY4MzYyNDQ0LCJuYmYiOjE2NjgzNjI0NDQsImp0aSI6IjkxMzhjNmE1LWJlOTQtNGNiMy1hYzMwLTRjYTRiNDEyZDM2ZSIsImV4cCI6MTY2ODM2NjA0NCwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZX0.8d3_1OZTvcG2XFNl1-HVVLXjtmg5YrLCvmVcOH-Ldgc",
    "token_type": "bearer"
}
```

---

#### Request:
```http request
GET /me
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0IiwiaWF0IjoxNjY4MzYyNDQ0LCJuYmYiOjE2NjgzNjI0NDQsImp0aSI6IjkxMzhjNmE1LWJlOTQtNGNiMy1hYzMwLTRjYTRiNDEyZDM2ZSIsImV4cCI6MTY2ODM2NjA0NCwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZX0.8d3_1OZTvcG2XFNl1-HVVLXjtmg5YrLCvmVcOH-Ldgc
```

#### Response:
```json
{
    "id": 1,
    "created": "2022-11-13T17:47:51.428216",
    "updated": "2022-11-13T17:47:51.428223",
    "username": "alperen",
    "email": "alperen@mail.com"
}
```

---

**Alperen Cubuk**
