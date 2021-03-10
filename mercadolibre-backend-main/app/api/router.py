from app.models.mercadolibre import Customer
from fastapi import APIRouter
from app.api.endpoints.mercadolibre import category, seller, product, customer, purchaseproduct

api_router = APIRouter()


api_router.include_router(seller.router, prefix = "/seller", tags = ["sellers"])
api_router.include_router(category.router, prefix = "/categories", tags = ["categories"])
api_router.include_router(product.router, prefix = "/product", tags = ["products"])
api_router.include_router(customer.router, prefix = "/customer", tags = ["customers"])
api_router.include_router(purchaseproduct.router, prefix = "/order", tags = ["orders"])