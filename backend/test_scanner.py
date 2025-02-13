import food_api

# Código de barras de prueba (puedes usar uno real)
BARCODE = "737628064502"  # Reemplázalo con un código real si tienes un producto

food_info = food_api.get_food_info(BARCODE)

if food_info:
    print("✅ Producto encontrado:")
    print(f"🔹 Nombre: {food_info['name']}")
    print(f"🔥 Calorías: {food_info['calories']} kcal")
    print(f"🍗 Proteínas: {food_info['proteins']} g")
    print(f"🍞 Carbohidratos: {food_info['carbs']} g")
    print(f"🍬 Azúcares: {food_info['sugars']} g")
    print(f"🛢️ Grasas: {food_info['fat']} g")
    print(f"🌾 Fibra: {food_info['fiber']} g")
    print(f"🧂 Sodio: {food_info['sodium']} mg")
else:
    print("❌ No se encontró el producto en la base de datos.")
