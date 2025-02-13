# backend/progress.py
import db
from datetime import datetime

def log_weight(user_id, weight):
    data = {"user_id": user_id, "weight": weight, "date": datetime.now().isoformat()}
    db.supabase.table("progress").insert(data).execute()
    return "Peso registrado exitosamente."
