# RecipeBook

## Стек
- Python
- Django
- djangorestframework

RecipeBook - это веб-приложение на основе Django, предназначенное для управления рецептами и продуктами. Приложение предоставляет REST API для добавления продуктов к рецептам, приготовления блюд по рецепту и отображения рецептов, в которых указанный продукт отсутствует или его количество меньше 10 грамм.

## Установка

Клонируйте репозиторий:

   ```bash
   git clone https://github.com/nikitaloshch/RecipeBook.git

cd backend

```
Cоздайте и активируйте виртуальное окружение:
```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows
    ```
    source venv/scripts/activate
    ```

Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Примените миграции:

```
python manage.py migrate
```

Запустите сервер :

```
python manage.py runserver
```
