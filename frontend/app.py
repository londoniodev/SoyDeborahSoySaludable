import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from screens.meals import MealsScreen
from screens.progress import ProgressScreen
from screens.notifications_config import NotificationsConfigScreen

# Definición de la paleta de colores
PRIMARY_COLOR = "#dd1587"
SECONDARY_COLOR = "#FFFFFF"

class NutritionApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title="MiAppNutricion")
        self.main_window.background_color = SECONDARY_COLOR

        # Crear el menú principal
        self.create_main_menu()
        self.main_window.show()

    def create_main_menu(self, widget=None):  # ✅ Ahora acepta un argumento opcional
        """Crea la pantalla del menú principal."""
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

        label = toga.Label("Bienvenido a MiAppNutricion", style=Pack(font_size=24, color=PRIMARY_COLOR, padding_bottom=10))

        # Botones del menú principal
        meals_button = toga.Button("🍽️ Registro de Comidas", on_press=self.go_meals, style=Pack(padding=10))
        progress_button = toga.Button("📊 Seguimiento de Progreso", on_press=self.go_progress, style=Pack(padding=10))
        reminders_button = toga.Button("⏰ Configurar Recordatorios", on_press=self.go_reminders, style=Pack(padding=10))

        # Agregar elementos
        main_box.add(label)
        main_box.add(meals_button)
        main_box.add(progress_button)
        main_box.add(reminders_button)

        self.main_window.content = main_box

    # Funciones para cambiar entre pantallas (ahora con opción de regreso)
    def go_meals(self, widget):
        self.main_window.content = MealsScreen(self.create_main_menu)  # ✅ Ahora funciona correctamente

    def go_progress(self, widget):
        self.main_window.content = ProgressScreen(self.create_main_menu)  # ✅ Ahora funciona correctamente

    def go_reminders(self, widget):
        self.main_window.content = NotificationsConfigScreen(self.create_main_menu)  # ✅ Ahora funciona correctamente

def main():
    return NutritionApp("MiAppNutricion", "org.example.nutricion")

if __name__ == '__main__':
    main().main_loop()

