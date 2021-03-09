from repository.order import OrderRepository
from model.order import OrderItemLine, Order, OrderItem, OrderItemVariant, Price
import uuid
from typing import List
from pydantic import BaseModel


def FindOrder(orderRepository: OrderRepository):
    return orderRepository.find()
