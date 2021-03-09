from pydantic import BaseModel
from typing import List


class Price(BaseModel):
    amount: float

    currency: str

    isTaxable: bool

    @staticmethod
    def create(amount: float, currency: str, isTaxable: bool):
        return Price(amount=amount, currency=currency, isTaxable=isTaxable)


class OrderItemVariant(BaseModel):
    price: Price

    @staticmethod
    def create(price: Price):
        return OrderItemVariant(price=price)


class OrderItem(BaseModel):
    itemId: str

    variant: OrderItemVariant

    @staticmethod
    def create(itemId: str, variant: OrderItemVariant):
        return OrderItem(itemId=itemId, variant=variant)


class OrderItemLine(BaseModel):
    item: OrderItem

    quantity: int

    @staticmethod
    def create(item: OrderItem, quantity: int):
        return OrderItemLine(item=item, quantity=quantity)


class Order(BaseModel):
    id: str

    items: List[OrderItemLine]

    def addItem(self, item: OrderItemLine):
        self.items.append(item=item)

    @staticmethod
    def create(id: str, items: List[OrderItemLine]):
        return Order(id=id, items=items)
