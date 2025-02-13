# frontend/screens/meals.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class MealsScreen(toga.Box):
    def __init__(self, go_back):
        super().__init__(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

        # Título de la pantalla
        title = toga.Label("🍽️ Registro de Comidas", style=Pack(font_size=24, padding_bottom=10))
        self.add(title)

        # Campo de entrada para el nombre de la comida
        self.food_input = toga.TextInput(placeholder="Ingrese el nombre del alimento...", style=Pack(padding=5, width=300))
        self.add(self.food_input)

        # Campo de entrada para las calorías
        self.calories_input = toga.TextInput(placeholder="Ingrese las calorías...", style=Pack(padding=5, width=300))
        self.add(self.calories_input)

        # Botón para registrar la comida
        self.submit_button = toga.Button("✅ Registrar Comida", on_press=self.register_meal, style=Pack(padding=10))
        self.add(self.submit_button)

        # Área de mensaje de confirmación
        self.message_label = toga.Label("", style=Pack(font_size=16, padding_top=10))
        self.add(self.message_label)

        # Botón de regreso al menú principal
        self.back_button = toga.Button("🔙 Volver al Menú", on_press=go_back, style=Pack(padding=10))
        self.add(self.back_button)

    def register_meal(self, widget):
        """Simula el registro de una comida."""
        food_name = self.food_input.value.strip()
        calories = self.calories_input.value.strip()

        if food_name and calories.isdigit():
            self.message_label.text = f"✅ Comida registrada: {food_name} ({calories} kcal)"
        else:
            self.message_label.text = "⚠️ Por favor, ingrese un alimento y calorías válidas."

def main():
    return MealsScreen()

