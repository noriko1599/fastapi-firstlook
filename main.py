from typing import Optional
from fastapi import FastAPI
from service.add_order import AddOrder, OrderRepository, AddOrderInput, OrderItemLine
from service.find_order import FindOrder

app = FastAPI()

orderRepository = OrderRepository()


@app.get("/")
def read_root():
    return 'ok'


@app.post('/order')
def add_order(input: AddOrderInput):

    return AddOrder(input=input, orderRepository=orderRepository)


@app.get('/order')
def find_order():

    return FindOrder(orderRepository=orderRepository)
