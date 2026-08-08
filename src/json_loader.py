import json
from pathlib import Path
from typing import List

from src.models import Category, Product


def load_categories_from_json(file_path: str) -> List[Category]:
    path = Path(file_path)

    # 1. Проверка существования файла
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            # Если JSON вообще не валиден — кидаем понятную ошибку
            raise json.JSONDecodeError(e.msg, e.doc, e.pos) from e

    # 2. Валидация структуры: должен быть список
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список категорий")

    categories = []
    for cat_data in data:
        # 3. Валидация каждой категории
        if not isinstance(cat_data, dict):
            continue  # raise ValueError, если хочим строже

        name = cat_data.get("name")
        description = cat_data.get("description", "")
        products_data = cat_data.get("products", [])

        if not name or not isinstance(products_data, list):
            continue  # пропускаем битые категории

        products = []
        for prod_data in products_data:
            if not isinstance(prod_data, dict):
                continue
            p_name = prod_data.get("name")
            p_desc = prod_data.get("description", "")
            p_price = prod_data.get("price")
            p_qty = prod_data.get("quantity")

            if p_name and isinstance(p_price, (int, float)) and isinstance(p_qty, int):
                products.append(Product(p_name, p_desc, float(p_price), p_qty))

        categories.append(Category(name, description, products))

    return categories
