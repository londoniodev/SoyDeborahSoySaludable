# backend/notifications.py
import sys
import os

# Agregar la carpeta 'backend' al path para poder importar módulos
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import time
import threading
from datetime import datetime
import db

def set_reminder(user_id, reminder_type, reminder_time, active=True):
    """
    Inserta o actualiza un recordatorio en la tabla 'reminders'.
    
    Se espera que reminder_time sea un string en formato "HH:MM" o "HH:MM:SS".
    Este valor se convertirá a "HH:MM:SS" antes de insertarlo en la base de datos.
    """
    # Intentar convertir reminder_time usando los dos formatos posibles
    try:
        # Primero se intenta con el formato "HH:MM"
        dt = datetime.strptime(reminder_time, "%H:%M")
    except ValueError:
        try:
            # Si falla, se intenta con el formato "HH:MM:SS"
            dt = datetime.strptime(reminder_time, "%H:%M:%S")
        except ValueError:
            raise ValueError("El formato de reminder_time es inválido. Debe ser 'HH:MM' o 'HH:MM:SS'.")
    
    # Formatear la hora a "HH:MM:SS"
    reminder_time_formatted = dt.strftime("%H:%M:%S")
    
    data = {
        "user_id": user_id,
        "reminder_type": reminder_type,
        "reminder_time": reminder_time_formatted,
        "active": active
    }
    
    print("Datos a insertar:", data)  # Debug: Verifica que el formato sea correcto
    response = db.supabase.table("reminders").upsert(data).execute()
    
    if response.data:
        return f"✅ Recordatorio guardado: {reminder_type} a las {reminder_time_formatted}."
    else:
        return "❌ Error: No se pudo guardar el recordatorio."

def get_reminders(user_id):
    """Obtiene los recordatorios activos de un usuario."""
    response = db.supabase.table("reminders")\
                .select("*")\
                .eq("user_id", user_id)\
                .eq("active", True)\
                .execute()
    return response.data

def reminder_daemon(user_id):
    """
    Hilo que revisa cada minuto si la hora actual coincide con algún recordatorio activo.
    """
    while True:
        # Se formatea la hora actual a "HH:MM:00" para comparar con el valor en la BD
        now = datetime.now().strftime("%H:%M:00")
        reminders = get_reminders(user_id)
        for r in reminders:
            if r["reminder_time"] == now:
                # En un MVP se puede imprimir un mensaje; para notificaciones reales se requiere integración nativa.
                print(f"Recordatorio: {r['reminder_type']} - ¡Es hora de registrar tus datos!")
        time.sleep(60)
