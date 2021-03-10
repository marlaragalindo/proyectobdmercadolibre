import os

TORTOISE_ORM = {
    "connections": {
        "default": os.environ.get("DATABASE_URL")
        },
    "apps": {
        "models": {
            "models": ["app.models.mercadolibre", "aerich.models"],
            "default_connection": "default",
        }
    },
}
