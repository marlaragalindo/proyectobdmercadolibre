from typing import List
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.models.mercadolibre import Category
from app.schemas.mercadolibre.Category import CategoryCreateSchema, CategorySchema

router = APIRouter()


@router.get("/", response_model = List[CategorySchema])
async def read_categories() -> List[CategorySchema]:
    return await CategorySchema.from_queryset(Category.all())


@router.get("/{category_id}", response_model = CategorySchema, responses = {404: {"model": HTTPNotFoundError}},)
async def get_category(category_id: int) -> CategorySchema:
    return await CategorySchema.from_queryset_single(Category.get(id = category_id))    


@router.post("/", response_model = CategorySchema)
async def create_category(category: CategoryCreateSchema) -> CategorySchema:
    new_category = await Category.create(**category.dict(exclude_unset=True))
    return await CategorySchema.from_tortoise_orm(new_category)


@router.put("/{category_id}", response_model = CategorySchema, responses = {404: {"model": HTTPNotFoundError}},)
async def update_category(category_id: int, category: CategoryCreateSchema):
    await Category.filter(id = category_id).update(**category.dict(exclude_unset = True))
    return await CategorySchema.from_queryset_single(Category.get(id = category_id))
