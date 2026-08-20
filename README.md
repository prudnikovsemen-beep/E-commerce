# E-commerce (Python 3.12)

Учебный проект по теме «Наследование и магические методы». Реализована базовая модель товаров и категорий с инкапсуляцией и валидацией.

## Реализованный функционал

- Классы: `Product`, `Smartphone`, `LawnGrass`, `Category`.
- Наследование: товары наследуются от базового класса `Product`.
- Инкапсуляция: приватные атрибуты (цена, список товаров) с `@property` и сеттерами.
- Магические методы: `__str__`, `__len__`, `__contains__`, `__iter__`, `__add__`.
- Глобальный счётчик товаров в категории с корректной изоляцией тестов.
- Загрузка данных из JSON-файла.

## Покрытие тестами

Покрытие функционального кода — **94%** (требование >75% выполнено).  
Отчёт о покрытии доступен в папке `htmlcov` (`htmlcov/index.html`).

## Запуск и проверки

```bash
poetry install
poetry run pytest --cov=src
poetry run flake8 src tests
poetry run mypy src

### Структура проекта
```bash

E-commerce/
├── .venv/                 # Виртуальное окружение (исключено из git)
├── htmlcov/               # Отчёт о покрытии тестами
│   └── index.html
├── data/                  # [Опционально] Папка с JSON-файлами
│   └── products.json
├── src/                   # Исходный код (пакет)
│   ├── __init__.py        # Инициализация пакета
│   ├── product.py         # Класс Product
│   ├── category.py        # Класс Category
│   ├── json_loader.py     # Загрузка и валидация JSON
│   └── models.py          # Базовые модели
├── tests/                 # Тесты
│   ├── conftest.py
│   ├── test_json_loader.py
│   ├── test_models.py
│   ├── test_product_category.py
│   └── test_product_category_magic.py
├── main.py                # Точка входа (в корне проекта)
├── pyproject.toml
├── .gitignore
└── README.md
