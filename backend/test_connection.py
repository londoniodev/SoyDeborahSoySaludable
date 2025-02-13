import db

# Intenta obtener todos los usuarios de la tabla 'users'
try:
    response = db.supabase.table("users").select("*").execute()
    print("✅ Conexión exitosa a Supabase!")
    print("🔍 Datos obtenidos:", response.data)
except Exception as e:
    print("❌ Error en la conexión:", e)
