import db
import meals
import progress
import notifications

# UUID del usuario en Supabase
USER_ID = "a9c2d8c7-72fb-44e7-9e0c-a93c2d3d2a76"

# Prueba insertar una comida
print(meals.add_meal(USER_ID, "Ensalada de Pollo", 250))

# Prueba registrar un nuevo peso
print(progress.log_weight(USER_ID, 68.5))

# Prueba configurar un recordatorio
print(notifications.set_reminder(USER_ID, "comidas", "12:30"))
