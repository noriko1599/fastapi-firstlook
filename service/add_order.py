from repository.order import OrderRepository
from model.order import OrderItemLine, Order, OrderItem, OrderItemVariant, Price
import uuid
from typing import List
from pydantic import BaseModel


class AddOrderInput(BaseModel):
    items: List[OrderItemLine]

    def isValid(self):
        if len(self.items) == 0:
            return False

        return True


def AddOrder(input: AddOrderInput, orderRepository: OrderRepository):
    if input.isValid() == False:
        raise Exception('Invalid input.')

    items: List[OrderItemLine] = []

    for itemLine in input.items:
        items.append(
            OrderItemLine.create(
                OrderItem.create(
                    itemId=itemLine.item.itemId,
                    variant=OrderItemVariant.create(
                        price=Price.create(
                            amount=itemLine.item.variant.price.amount,
                            currency=itemLine.item.variant.price.currency,
                            isTaxable=itemLine.item.variant.price.isTaxable
                        )
                    )
                ),
                quantity=itemLine.quantity
            )
        )

    order: Order = Order.create(id=str(uuid.uuid4()), items=items)

    return orderRepository.add(order=order)
