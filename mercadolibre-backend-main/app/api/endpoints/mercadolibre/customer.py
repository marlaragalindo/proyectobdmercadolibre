from typing import List
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.models.mercadolibre import Customer
from app.schemas.mercadolibre.Customer import CustomerCreateSchema, CustomerSchema, CustomerPlainSchema

router = APIRouter()

@router.get("/", response_model = List[CustomerPlainSchema])
async def read_customers() -> List[CustomerPlainSchema]:
    return await CustomerPlainSchema.from_queryset(Customer.all())


@router.get("/{customer_id}", response_model = CustomerPlainSchema, responses = {404: {"model": HTTPNotFoundError}},)
async def get_customer(customer_id: int) -> CustomerPlainSchema:
    return await CustomerPlainSchema.from_queryset_single(Customer.get(id = customer_id)) 


@router.post("/", response_model = CustomerSchema)
async def create_customer(customer: CustomerCreateSchema) -> CustomerSchema:
    new_customer = await Customer.create(**customer.dict(exclude_unset = True))
    return await CustomerSchema.from_tortoise_orm(new_customer) 
 

@router.put("/{customer_id}", response_model = CustomerPlainSchema, responses = {404: {"model": HTTPNotFoundError}},)
async def update_customer(customer_id: int, customer: CustomerCreateSchema):
    await Customer.filter(id = customer_id).update(**customer.dict(exclude_unset = True))
    return await CustomerPlainSchema.from_queryset_single(Customer.get(id = customer_id))
