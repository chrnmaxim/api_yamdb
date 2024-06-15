# REST API для YaMDb

Проект YaMDb собирает отзывы пользователей на произведения. 

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 

Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 

Добавлять произведения, категории и жанры может только администратор.

Пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

> [!NOTE]
> Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

## Технологии:
* Python 3.11
* Django 3.2.16
* Django REST framework 3.12.4
* djangorestframework-simplejwt 4.7.2

## Авторы
* https://github.com/eXistenZKing (Python backend разработчик)
* https://github.com/BOSSISS (Python backend разработчик)
* https://github.com/chrnmaxim (Python backend разработчик, teamlead)

## Запуск проекта

Клонировать проект c GitHub:

```bash
git clone git@github.com:chrnmaxim/api_yamdb.git
```

Перейти в папку с проектом:

```bash
cd api_yamdb
```
Установить виртуальное окружение:
```bash
python -m venv venv
```
Активировать виртуальное окружениe:
```bash
. venv/Scripts/activate
```
Обновить менеджер пакетов pip:
```bash
python -m pip install --upgrade pip
```
Установить зависимости из requirements.txt:
```bash
pip install -r requirements.txt
``` 
Перейти в директорию с файлом manage.py и применить миграции:
```bash
cd api_yamdb
python manage.py migrate
``` 
Создать супер пользователя:

```bash
python manage.py createsuperuser
```
Запустить сервер разработки (виртуальное окружение должно быть активно):
```bash
python manage.py runserver 
```
Документация API в формате ReDoc будет доступна по адресу:
```bash
http://127.0.0.1:8000/redoc/
```

## Алгоритм регистрации пользователей
1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
2. YaMDB отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес `email`.
3. Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт` /api/v1/auth/token/`, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле (описание полей — в документации).

## Пользовательские роли
* Аноним — может просматривать описания произведений, читать отзывы и комментарии.
* Аутентифицированный пользователь (`user`) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
* Модератор (`moderator`) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
* Администратор (`admin`) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
* Суперюзер Django — обладет правами администратора (`admin`)

## Примеры запросов

### Регистрация нового пользователя
Получить код подтверждения на переданный `email`. Права доступа: Доступно без токена. Использовать имя 'me' в качестве username `запрещено`.

POST `http://127.0.0.1:8000/api/v1/auth/signup/`
```bash
{
  "email": "user@example.com",
  "username": "^w\\Z"
}
```

### Получение JWT-токена
Получение JWT-токена в обмен на `username` и `confirmation_code`. Права доступа: Доступно без токена.

POST `http://127.0.0.1:8000/api/v1/auth/token/`
```bash
{
  "username": "^w\\Z",
  "confirmation_code": "string"
}
```

### Получение списка всех произведений
Получить список всех произведений, к которым пишут отзывы (определённый фильм, книга или песенка). Права доступа: Доступно без токена

GET `http://127.0.0.1:8000/api/v1/titles/`

### Получение списка всех отзывов
Получить список всех отзывов. Права доступа: Доступно без токена.

GET `http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/`

### Добавление нового отзываа
Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение. Права доступа: Аутентифицированные пользователи.

POST `http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/`
```bash
{
  "text": "string",
  "score": 1
}
```

### Получение списка всех комментариев к отзыву
олучить список всех комментариев к отзыву по id Права доступа: Доступно без токена.

GET `http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/`

### Добавление комментария к отзыву
Добавить новый комментарий для отзыва. Права доступа: Аутентифицированные пользователи.

POST `http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/`
```bash
{
  "text": "string"
}
```
> [!TIP]
> К доступным эндпоинтам также можно обращаться с помощью [Postman](https://www.postman.com/).