from tortoise import fields
from tortoise.models import Model
from enum import Enum


class PaymentMethod(str, Enum):
    transfer = "transfer"
    credit = "credit"
    debit = "debit"


class Seller(Model):
    name = fields.CharField(max_length = 255)
    address = fields.CharField(max_length = 255)
    phone = fields.IntField()
    password = fields.CharField(max_length = 64)

    products: fields.ReverseRelation["Product"]

    class Meta:
        ordering = ["name"]


class Product(Model):
    name = fields.CharField(max_length = 128)
    price = fields.FloatField()
    date = fields.DatetimeField(auto_now_add = True)
    stock = fields.IntField()
    category = fields.ForeignKeyField("models.Category", on_delete = "CASCADE", related_name = "products")
    seller = fields.ForeignKeyField("models.Seller", on_delete = "CASCADE", related_name = "products")

    orders: fields.ReverseRelation["PurchaseProduct"]
    
    class Meta:
        ordering = ["-date"] 


class Category(Model):
    name = fields.CharField(max_length = 32)

    products: fields.ReverseRelation["Product"]

    class Meta:
        ordering = ["name"]

    class PydanticMeta:
        exclude = ("products", )
    


class PurchaseProduct(Model):
    quantity = fields.IntField()
    payment_method: PaymentMethod = fields.CharEnumField(PaymentMethod, max_length = 16)
    date = fields.DatetimeField(auto_now_add = True)
    product = fields.ForeignKeyField("models.Product", on_delete = "CASCADE", related_name = "orders")
    customer =  fields.ForeignKeyField("models.Customer", on_delete = "CASCADE", related_name = "orders")

    class Meta:
        ordering = ["-date"]


class Customer(Model):
    name = fields.CharField(max_length = 255)
    address = fields.CharField(max_length = 255)
    phone = fields.IntField()
    password = fields.CharField(max_length = 64)

    orders: fields.ReverseRelation["PurchaseProduct"]

    class Meta:
        ordering = ["name"]