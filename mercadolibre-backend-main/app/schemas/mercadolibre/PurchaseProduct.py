from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models import mercadolibre

Tortoise.init_models(["app.models.mercadolibre"], "models")

OrderSchema = pydantic_model_creator(mercadolibre.PurchaseProduct, name = "Order")

OrderCreateSchema = pydantic_model_creator(mercadolibre.PurchaseProduct, name = "OrderCreate", exclude = ("id", "date", ), exclude_readonly = True)

OrderPlainSchema = pydantic_model_creator(mercadolibre.PurchaseProduct, name = "OrderPlain", exclude = ("product", "seller", "customer", ))
