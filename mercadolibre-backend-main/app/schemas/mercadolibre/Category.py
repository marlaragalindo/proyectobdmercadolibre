from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models import mercadolibre


Tortoise.init_models(["app.models.mercadolibre"], "models")

CategorySchema = pydantic_model_creator(mercadolibre.Category, name = "Category")

CategoryCreateSchema = pydantic_model_creator(mercadolibre.Category, name = "CategoryCreate", exclude = ("id", ))

 