# backend/db.py
import os
from supabase import create_client, Client

SUPABASE_URL = "https://tyydjcsrlhzcwoqzygks.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR5eWRqY3NybGh6Y3dvcXp5Z2tzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczODk2Njg4OSwiZXhwIjoyMDU0NTQyODg5fQ.s0vBRNMbAhj0W1fprpI2IpcPclgR13bXkXtUnrFsDR8"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
