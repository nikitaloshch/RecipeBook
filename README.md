[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

# RecipeBook

RecipeBook - это веб-приложение на основе Django, предназначенное для управления рецептами и продуктами. Приложение предоставляет REST API для добавления продуктов к рецептам, приготовления блюд по рецепту и отображения рецептов, в которых указанный продукт отсутствует или его количество меньше 10 грамм.

### Стек
- Python
- Django
- djangorestframework

## Установка

Клонируйте репозиторий:

   ```bash
   git clone https://github.com/nikitaloshch/RecipeBook.git

cd backend

```
Cоздайте и активируйте виртуальное окружение:
```bash
python -m venv venv
```

* Если у вас Linux/macOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows
    ```bash
    source venv/scripts/activate
    ```

Установите зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Примените миграции:

```bash
python manage.py migrate
```

Запустите сервер:

```bash
python manage.py runserver
```

## Использование

Добавление продукта к рецепту:

```bash
http://127.0.0.1:8000/add_product_to_recipe/<recipe_id>/<product_id>/<weight>/
```

Приготовление блюда по рецепту:

```bash
http://127.0.0.1:8000/cook_recipe/<recipe_id>/
```

Отображение рецептов без указанного продукта:

```bash
http://127.0.0.1:8000/show_recipes_without_product/<product_id>/
```

## Админка 

Создайте админа:

```bash
python manage.py createsuperuser
```

Перейдите в админку и создайте продукты и рецепты:

```bash
http://127.0.0.1:8000/admin/
```
