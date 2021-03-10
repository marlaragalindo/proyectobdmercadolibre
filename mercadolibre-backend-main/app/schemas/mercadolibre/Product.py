from typing import Optional
from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models import mercadolibre

Tortoise.init_models(["app.models.mercadolibre"], "models")

ProductSchema = pydantic_model_creator(mercadolibre.Product, name = "Product")

ProductCreateSchema = pydantic_model_creator(mercadolibre.Product, name = "ProductCreate", exclude = ("id", "date", ), exclude_readonly = True)

ProductPlainSchema = pydantic_model_creator(mercadolibre.Product, name = "ProductPlain", exclude = ("seller", "orders", "seller_id", ))
