# frontend/screens/profile.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class ProfileScreen(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))
        label = toga.Label("Perfil del Usuario", style=Pack(font_size=24, padding_bottom=10))
        self.add(label)
        # Se agregarían formularios para ingresar peso, altura, edad, etc.

def main():
    return ProfileScreen()
