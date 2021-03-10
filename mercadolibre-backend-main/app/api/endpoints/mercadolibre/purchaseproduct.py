from typing import List
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.models.mercadolibre import PurchaseProduct, Product
from app.schemas.mercadolibre.PurchaseProduct import OrderCreateSchema, OrderSchema, OrderPlainSchema
from app.schemas.mercadolibre.Product import ProductCreateSchema, ProductSchema

router = APIRouter()

@router.get("/", response_model = List[OrderPlainSchema])
async def read_orders() -> List[OrderPlainSchema]:
    return await OrderPlainSchema.from_queryset(PurchaseProduct.all())


@router.get("/{order_id}", response_model = OrderPlainSchema, responses = {404: {"model": HTTPNotFoundError}},)
async def get_order(order_id: int) -> OrderPlainSchema:
    return await OrderPlainSchema.from_queryset_single(PurchaseProduct.get(id = order_id))


@router.post("/", response_model = OrderPlainSchema, responses = {404: {"model": HTTPNotFoundError}},)
async def create_order(order: OrderCreateSchema) -> OrderSchema:
    temp_order = await PurchaseProduct(**order.dict(exclude_unset = True))
    product = await Product.get(id = temp_order.product_id)
    product_py = await ProductCreateSchema.from_tortoise_orm(product)

    if product_py.stock >= temp_order.quantity:
        product_py.stock -= temp_order.quantity
        await Product.filter(id = temp_order.product_id).update(**product_py.dict(exclude_unset = True))
        await temp_order.save()
        return await OrderPlainSchema.from_tortoise_orm(temp_order)
    else:
        print(f"No hay stock, compraste {temp_order.quantity} y solo quedan {product_py.stock}")




#   await temp_order.save()
#    await Product.filter(id=product_id).update(**product_py.dict(exclude_unset=True))

#    new_order = await PurchaseProduct.create(**order.dict(exclude_unset = True)) 
#    if product.stock > new_order.quantity:
#        product.stock -= new_order.quantity
#        product_py = ProductCreateSchema.from_tortoise_orm(product)
#        await Product.filter(id=product_id).update(**product_py.dict(exclude_unset=True))
#       return await OrderSchema.from_tortoise_orm(new_order)
#    else:
#        return {"message":"Error xdd"}
