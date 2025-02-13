# backend/meals.py
import db

def add_meal(user_id, food_name, calories):
    data = {"user_id": user_id, "food_name": food_name, "calories": calories}
    db.supabase.table("meals").insert(data).execute()
    return "Comida registrada exitosamente."
