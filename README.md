# api_final

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```git clone git@github.com:yasinalizade/api_final_yatube.git```
```cd api_final_yatube```

Cоздать и активировать виртуальное окружение:
```python3 -m venv venv```
```source venv/bin/activate```
Установить зависимости из файла requirements.txt:
```python3 -m pip install --upgrade pip```

```pip install -r requirements.txt```

Выполнить миграции:
```python3 manage.py migrate```

Запустить проект:
```python3 manage.py runserver```

## Как посмотреть все urls api:

К проекту подключена библиотека drf-yasg для автоматического обновления документации API:

[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
