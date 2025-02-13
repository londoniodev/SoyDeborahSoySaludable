# backend/mercadopago_service.py
import mercadopago
import os

# Configura MercadoPago con tu ACCESS_TOKEN (puedes usar variables de entorno)
mp = mercadopago.SDK(os.getenv("MERCADOPAGO_ACCESS_TOKEN", "tu_access_token"))

def create_payment_link(user_id, email, plan="monthly"):
    """
    Genera un link de pago para la suscripción premium.
    Plan 'monthly' cuesta 25.000 COP y 'annual' 225.000 COP (25% OFF).
    """
    if plan == "monthly":
        price = 25000
        title = "Suscripción Mensual"
    else:
        price = 225000
        title = "Suscripción Anual (25% OFF)"

    preference_data = {
        "items": [
            {
                "title": title,
                "quantity": 1,
                "unit_price": float(price),
                "currency_id": "COP",
            }
        ],
        "payer": {
            "email": email
        },
        "back_urls": {
            "success": "https://tuapp.com/success",
            "failure": "https://tuapp.com/failure",
            "pending": "https://tuapp.com/pending"
        },
        "auto_return": "approved",
        "metadata": {"user_id": user_id, "plan": plan},
    }

    preference = mp.preference().create(preference_data)
    return preference["response"]["init_point"]
