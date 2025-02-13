import sys
import os

# Agregar la carpeta 'backend' al path para que Python pueda encontrarla
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
import backend.notifications as notifications
from datetime import datetime

# Listas de opciones para la selección de hora
HOURS = [str(h).zfill(2) for h in range(1, 13)]    # "01" a "12"
MINUTES = [str(m).zfill(2) for m in range(0, 60, 5)]  # "00", "05", "10", ... "55"
PERIODS = ["AM", "PM"]

class NotificationsConfigScreen(toga.Box):
    def __init__(self, go_back):
        super().__init__(style=Pack(direction="column", alignment="center", padding=20))

        # Título de la pantalla
        title = toga.Label("🔔 Configuración de Recordatorios", style=Pack(font_size=24, padding_bottom=10))
        self.add(title)

        # Entrada para el recordatorio
        self.reminder_input = toga.TextInput(
            placeholder="Ej: Tomar vitaminas",
            style=Pack(width=300, padding_bottom=10)
        )
        self.add(self.reminder_input)

        # Selectores para la hora
        self.hour_picker = toga.Selection(items=HOURS, style=Pack(width=80, padding_right=5))
        self.minute_picker = toga.Selection(items=MINUTES, style=Pack(width=80, padding_right=5))
        self.period_picker = toga.Selection(items=PERIODS, style=Pack(width=80))

        time_box = toga.Box(style=Pack(direction="row", alignment="center", padding_bottom=10))
        time_box.add(self.hour_picker)
        time_box.add(toga.Label(":", style=Pack(font_size=20, padding_right=5)))
        time_box.add(self.minute_picker)
        time_box.add(self.period_picker)
        self.add(time_box)

        # Botón para guardar el recordatorio
        self.save_button = toga.Button(
            "✅ Guardar Recordatorio",
            on_press=self.save_reminder,
            style=Pack(padding_bottom=10)
        )
        self.add(self.save_button)

        # Mensaje de confirmación o error
        self.message_label = toga.Label("", style=Pack(font_size=16, padding_top=10))
        self.add(self.message_label)

        # Botón para regresar al menú
        self.back_button = toga.Button(
            "🔙 Volver al Menú",
            on_press=go_back,
            style=Pack(padding=10)
        )
        self.add(self.back_button)

    def save_reminder(self, widget):
        """
        Convierte la hora seleccionada al formato 24 horas y guarda el recordatorio.
        """
        user_id = "a9c2d8c7-72fb-44e7-9e0c-a93c2d3d2a76"  # UUID real del usuario
        reminder_text = self.reminder_input.value.strip()
        hour = self.hour_picker.value
        minute = self.minute_picker.value
        period = self.period_picker.value

        # Validaciones
        if not reminder_text:
            self.message_label.text = "⚠️ Por favor, ingrese un recordatorio."
            return

        if not hour or not minute or not period:
            self.message_label.text = "⚠️ Seleccione una hora válida."
            return

        try:
            # Se arma el string de hora en formato 12 horas, por ejemplo "01:00 AM"
            time_12h = f"{hour}:{minute} {period}"
            # Se parsea al objeto datetime y luego se extrae la parte de la hora
            dt_obj = datetime.strptime(time_12h, "%I:%M %p")
            time_obj = dt_obj.time()  # Esto es un objeto time, cuyo str(time_obj) dará "HH:MM:SS"
            print("Valor de time_obj:", time_obj)  # Debug: Debe imprimir algo como "13:00:00" para 1:00 PM

            # Se guarda el recordatorio en la base de datos
            notifications.set_reminder(user_id, reminder_text, time_obj, active=True)
            self.message_label.text = f"✅ Recordatorio guardado: {reminder_text} a las {time_obj.strftime('%H:%M:%S')}."
        except ValueError as e:
            print("Error al convertir la hora:", e)
            self.message_label.text = "⚠️ Error en la conversión de la hora. Intente nuevamente."

def main():
    # Se define una función dummy para 'go_back' para este ejemplo.
    return NotificationsConfigScreen(go_back=lambda widget: None)