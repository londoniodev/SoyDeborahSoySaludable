# frontend/screens/home.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW

PRIMARY_COLOR = "#dd1587"
SECONDARY_COLOR = "#FFFFFF"

class HomeScreen(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, alignment=CENTER, padding=20, background_color=SECONDARY_COLOR))
        label = toga.Label("Inicio", style=Pack(font_size=24, color=PRIMARY_COLOR, padding_bottom=10))
        self.add(label)
        # Aquí se pueden agregar más componentes del inicio.

def main():
    return HomeScreen()
