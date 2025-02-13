# frontend/screens/progress.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class ProgressScreen(toga.Box):
    def __init__(self, go_back):
        super().__init__(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

        # Título de la pantalla
        title = toga.Label("📊 Seguimiento de Progreso", style=Pack(font_size=24, padding_bottom=10))
        self.add(title)

        # Campo de entrada para el peso actual
        self.weight_input = toga.TextInput(placeholder="Ingrese su peso actual (kg)...", style=Pack(padding=5, width=300))
        self.add(self.weight_input)

        # Botón para registrar el peso
        self.submit_button = toga.Button("✅ Registrar Peso", on_press=self.register_weight, style=Pack(padding=10))
        self.add(self.submit_button)

        # Área de mensaje de confirmación
        self.message_label = toga.Label("", style=Pack(font_size=16, padding_top=10))
        self.add(self.message_label)

        # Sección para visualizar historial de peso (simulación)
        self.history_label = toga.Label("📅 Historial de Peso:", style=Pack(font_size=20, padding_top=15))
        self.add(self.history_label)
        self.history_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=10))
        self.add(self.history_box)

        # Botón de regreso al menú principal
        self.back_button = toga.Button("🔙 Volver al Menú", on_press=go_back, style=Pack(padding=10))
        self.add(self.back_button)

    def register_weight(self, widget):
        """Simula el registro del peso."""
        weight = self.weight_input.value.strip()

        if weight.replace('.', '', 1).isdigit():
            self.message_label.text = f"✅ Peso registrado: {weight} kg"
            self.history_box.add(toga.Label(f"📌 {weight} kg registrado.", style=Pack(padding=5)))
        else:
            self.message_label.text = "⚠️ Por favor, ingrese un peso válido."

def main():
    return ProgressScreen()
