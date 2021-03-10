from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models import mercadolibre

Tortoise.init_models(["app.models.mercadolibre"], "models")

CustomerSchema = pydantic_model_creator(mercadolibre.Customer, name = "Customer")

CustomerCreateSchema = pydantic_model_creator(mercadolibre.Customer, name = "CustomerCreate", exclude = ("id", "orders", ), exclude_readonly = True)

CustomerPlainSchema = pydantic_model_creator(mercadolibre.Customer, name = "CustomerPlain", exclude = ("orders", ))
