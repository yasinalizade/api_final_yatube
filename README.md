# api_final

## Описание

Проект API для социальной сети YaTube. 

## Установка

### Клонировать репозиторий и перейти в него в командной строке:

```git clone git@github.com:yasinalizade/api_final_yatube.git```
```cd api_final_yatube```

### Cоздать и активировать виртуальное окружение:

```python -m venv venv```

```source venv/bin/activate```

### Установить зависимости из файла requirements.txt:

```python3 -m pip install --upgrade pip```

```pip install -r requirements.txt```

### Выполнить миграции:

```python manage.py migrate```

### Запустить проект:

```python3 manage.py runserver```

## Как посмотреть работу всех urls api:

К проекту подключена библиотека drf-yasg для автоматического обновления документации API:

[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

## Стек технологий

* Python 3.9
* Django 2.2.16
* Django Rest Framework 3.12.4
* Simple-JWT 4.7.2
