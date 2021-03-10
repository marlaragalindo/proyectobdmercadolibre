from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models import mercadolibre

Tortoise.init_models(["app.models.mercadolibre"], "models")

SellerSchema = pydantic_model_creator(mercadolibre.Seller, name = "Seller")

SellerCreateSchema = pydantic_model_creator(mercadolibre.Seller, name = "SellerCreate", exclude = ("id", "products", ), exclude_readonly = True)

SellerPlainSchema = pydantic_model_creator(mercadolibre.Seller, name = "SellerPlain", exclude = ("products", ))

SellerProductSchema = pydantic_model_creator(mercadolibre.Seller, name = "SellerProduct", exclude = ("products.orders", )) 