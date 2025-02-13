# backend/auth.py
import db

def register_user(email, password):
    response = db.supabase.auth.sign_up({"email": email, "password": password})
    return response

def login_user(email, password):
    response = db.supabase.auth.sign_in_with_password({"email": email, "password": password})
    return response
