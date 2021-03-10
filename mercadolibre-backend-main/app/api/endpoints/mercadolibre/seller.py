from typing import List
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.models.mercadolibre import Seller
from app.schemas.mercadolibre.Seller import SellerCreateSchema, SellerSchema, SellerPlainSchema, SellerProductSchema

router = APIRouter()

@router.get("/", response_model = List[SellerPlainSchema])
async def read_sellers() -> List[SellerPlainSchema]:
    return await SellerPlainSchema.from_queryset(Seller.all())
   

@router.get("/{seller_id}", response_model = SellerPlainSchema, responses = {404: {"model": HTTPNotFoundError}},)
async def get_seller(seller_id: int) -> SellerPlainSchema:
    return await SellerPlainSchema.from_queryset_single(Seller.get(id = seller_id)) 


@router.post("/", response_model = SellerSchema)
async def create_seller(seller: SellerCreateSchema) -> SellerSchema:
    new_seller = await Seller.create(**seller.dict(exclude_unset = True))
    return await SellerSchema.from_tortoise_orm(new_seller)


@router.put("/{seller_id}", response_model = SellerPlainSchema, responses = {404: {"model": HTTPNotFoundError}},)
async def update_seller(seller_id: int, seller: SellerCreateSchema):
    await Seller.filter(id = seller_id).update(**seller.dict(exclude_unset = True))
    return await SellerPlainSchema.from_queryset_single(Seller.get(id = seller_id))
