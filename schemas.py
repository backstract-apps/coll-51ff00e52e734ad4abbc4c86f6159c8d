from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Products(BaseModel):
    id: Any
    name: str
    description: str
    price: float
    image_url: str
    category_id: int


class ReadProducts(BaseModel):
    id: Any
    name: str
    description: str
    price: float
    image_url: str
    category_id: int
    class Config:
        from_attributes = True


class Categories(BaseModel):
    id: Any
    name: str


class ReadCategories(BaseModel):
    id: Any
    name: str
    class Config:
        from_attributes = True


class Customers(BaseModel):
    id: Any
    name: str
    address: str
    contact_info: str


class ReadCustomers(BaseModel):
    id: Any
    name: str
    address: str
    contact_info: str
    class Config:
        from_attributes = True


class Orders(BaseModel):
    id: Any
    order_date: Any
    shipping_address: str
    total_cost: float
    customer_id: int


class ReadOrders(BaseModel):
    id: Any
    order_date: Any
    shipping_address: str
    total_cost: float
    customer_id: int
    class Config:
        from_attributes = True


class OrderItems(BaseModel):
    id: Any
    order_id: int
    product_id: int
    quantity: int


class ReadOrderItems(BaseModel):
    id: Any
    order_id: int
    product_id: int
    quantity: int
    class Config:
        from_attributes = True




class PostOrders(BaseModel):
    id: int
    order_date: str
    shipping_address: str
    total_cost: str
    customer_id: int

    class Config:
        from_attributes = True



class PostCategories(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True



class PostCustomers(BaseModel):
    id: int
    name: str
    address: str
    contact_info: str

    class Config:
        from_attributes = True



class PostOrderItems(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True



class PostProducts(BaseModel):
    id: int
    name: str
    description: str
    price: str
    image_url: str
    category_id: int

    class Config:
        from_attributes = True

