from typing import List
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.models.mercadolibre import Product
from app.schemas.mercadolibre.Product import ProductCreateSchema, ProductSchema, ProductPlainSchema

router = APIRouter()

@router.get("/", response_model = List[ProductPlainSchema])
async def read_products() -> List[ProductPlainSchema]:
    return await ProductPlainSchema.from_queryset(Product.all())


@router.get("/{product_id}", response_model = ProductPlainSchema, responses = {404: {"model": HTTPNotFoundError}},)
async def get_product(product_id: int) -> ProductPlainSchema:
    return await ProductPlainSchema.from_queryset_single(Product.get(id = product_id))    


@router.post("/", response_model = ProductSchema)
async def create_product(product: ProductCreateSchema) -> ProductSchema:
    new_product = await Product.create(**product.dict(exclude_unset = True))
    return await ProductSchema.from_tortoise_orm(new_product)


@router.put("/{product_id}", response_model = ProductPlainSchema, responses = {404: {"model": HTTPNotFoundError}},)
async def update_product(product_id: int, product: ProductCreateSchema):
    await Product.filter(id = product_id).update(**product.dict(exclude_unset = True))
    return await ProductPlainSchema.from_queryset_single(Product.get(id = product_id))

