# backend/food_api.py
import requests

def get_food_info(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "product" in data:
            product = data["product"]
            nutrition_info = product.get("nutriments", {})
            return {
                "name": product.get("product_name", "Desconocido"),
                "calories": nutrition_info.get("energy-kcal_100g", 0),
                "proteins": nutrition_info.get("proteins_100g", 0),
                "carbs": nutrition_info.get("carbohydrates_100g", 0),
                "sugars": nutrition_info.get("sugars_100g", 0),
                "fat": nutrition_info.get("fat_100g", 0),
                "fiber": nutrition_info.get("fiber_100g", 0),
                "sodium": nutrition_info.get("sodium_100g", 0)
            }
    return None
