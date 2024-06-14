# REST API для YaMDb

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

### Технологии:
* Python 3.11
* Django 3.2.16
* Django REST framework 3.12.4
* djangorestframework-simplejwt 4.7.2

### Запуск проекта

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
Документация API в формате ReDoc доступна по адресу:
```bash
http://127.0.0.1:8000/redoc/
```

### Авторы
* https://github.com/eXistenZKing (Python backend разработчик)
* https://github.com/BOSSISS (Python backend разработчик)
* https://github.com/chrnmaxim (Python backend разработчик, teamlead)
