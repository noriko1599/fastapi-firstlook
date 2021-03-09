from model.order import Order
from typing import List


class OrderRepository:
    _records = []

    def add(self, order: Order):
        self._records.append(order)
        return order

    def remove(self, order: Order):
        self._records.remove(order)
        return order

    def find(self):
        return self._records
