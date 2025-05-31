from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_products(db: Session):

    query = db.query(models.Products)

    products_all = query.all()
    products_all = (
        [new_data.to_dict() for new_data in products_all]
        if products_all
        else products_all
    )
    res = {
        "products_all": products_all,
    }
    return res


async def post_orders(db: Session, raw_data: schemas.PostOrders):
    id: int = raw_data.id
    order_date: str = raw_data.order_date
    shipping_address: str = raw_data.shipping_address
    total_cost: str = raw_data.total_cost
    customer_id: int = raw_data.customer_id

    record_to_be_added = {
        "id": id,
        "order_date": order_date,
        "total_cost": total_cost,
        "customer_id": customer_id,
        "shipping_address": shipping_address,
    }
    new_orders = models.Orders(**record_to_be_added)
    db.add(new_orders)
    db.commit()
    db.refresh(new_orders)
    orders_inserted_record = new_orders.to_dict()

    vhnbnmb = aliased(models.OrderItems)
    query = db.query(models.Orders, vhnbnmb)

    query = query.join(vhnbnmb, and_(models.Orders.order_date == models.Orders.id))

    mnnvnbvnb = query.all()
    mnnvnbvnb = (
        [
            {
                "mnnvnbvnb_1": s1.to_dict() if hasattr(s1, "to_dict") else s1.__dict__,
                "mnnvnbvnb_2": s2.to_dict() if hasattr(s2, "to_dict") else s2.__dict__,
            }
            for s1, s2 in mnnvnbvnb
        ]
        if mnnvnbvnb
        else mnnvnbvnb
    )
    res = {
        "orders_inserted_record": orders_inserted_record,
        " nvnmbmnb": mnnvnbvnb,
    }
    return res


async def get_products_id(db: Session, id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.id == id))

    products_one = query.first()

    products_one = (
        (
            products_one.to_dict()
            if hasattr(products_one, "to_dict")
            else vars(products_one)
        )
        if products_one
        else products_one
    )

    res = {
        "products_one": products_one,
    }
    return res


async def put_products_id(
    db: Session,
    id: int,
    name: str,
    description: str,
    price: str,
    image_url: str,
    category_id: int,
):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.id == id))
    products_edited_record = query.first()

    if products_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "price": price,
            "image_url": image_url,
            "category_id": category_id,
            "description": description,
        }.items():
            setattr(products_edited_record, key, value)

        db.commit()
        db.refresh(products_edited_record)

        products_edited_record = (
            products_edited_record.to_dict()
            if hasattr(products_edited_record, "to_dict")
            else vars(products_edited_record)
        )
    res = {
        "products_edited_record": products_edited_record,
    }
    return res


async def delete_products_id(db: Session, id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        products_deleted = record_to_delete.to_dict()
    else:
        products_deleted = record_to_delete
    res = {
        "products_deleted": products_deleted,
    }
    return res


async def get_categories(db: Session):

    query = db.query(models.Categories)

    categories_all = query.all()
    categories_all = (
        [new_data.to_dict() for new_data in categories_all]
        if categories_all
        else categories_all
    )
    res = {
        "categories_all": categories_all,
    }
    return res


async def get_categories_id(db: Session, id: int):

    query = db.query(models.Categories)
    query = query.filter(and_(models.Categories.id == id))

    categories_one = query.first()

    categories_one = (
        (
            categories_one.to_dict()
            if hasattr(categories_one, "to_dict")
            else vars(categories_one)
        )
        if categories_one
        else categories_one
    )

    res = {
        "categories_one": categories_one,
    }
    return res


async def post_categories(db: Session, raw_data: schemas.PostCategories):
    id: int = raw_data.id
    name: str = raw_data.name

    record_to_be_added = {"id": id, "name": name}
    new_categories = models.Categories(**record_to_be_added)
    db.add(new_categories)
    db.commit()
    db.refresh(new_categories)
    categories_inserted_record = new_categories.to_dict()

    res = {
        "categories_inserted_record": categories_inserted_record,
    }
    return res


async def put_categories_id(db: Session, id: int, name: str):

    query = db.query(models.Categories)
    query = query.filter(and_(models.Categories.id == id))
    categories_edited_record = query.first()

    if categories_edited_record:
        for key, value in {"id": id, "name": name}.items():
            setattr(categories_edited_record, key, value)

        db.commit()
        db.refresh(categories_edited_record)

        categories_edited_record = (
            categories_edited_record.to_dict()
            if hasattr(categories_edited_record, "to_dict")
            else vars(categories_edited_record)
        )
    res = {
        "categories_edited_record": categories_edited_record,
    }
    return res


async def delete_categories_id(db: Session, id: int):

    query = db.query(models.Categories)
    query = query.filter(and_(models.Categories.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        categories_deleted = record_to_delete.to_dict()
    else:
        categories_deleted = record_to_delete
    res = {
        "categories_deleted": categories_deleted,
    }
    return res


async def get_customers(db: Session):

    query = db.query(models.Customers)

    customers_all = query.all()
    customers_all = (
        [new_data.to_dict() for new_data in customers_all]
        if customers_all
        else customers_all
    )
    res = {
        "customers_all": customers_all,
    }
    return res


async def get_customers_id(db: Session, id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.id == id))

    customers_one = query.first()

    customers_one = (
        (
            customers_one.to_dict()
            if hasattr(customers_one, "to_dict")
            else vars(customers_one)
        )
        if customers_one
        else customers_one
    )

    res = {
        "customers_one": customers_one,
    }
    return res


async def post_customers(db: Session, raw_data: schemas.PostCustomers):
    id: int = raw_data.id
    name: str = raw_data.name
    address: str = raw_data.address
    contact_info: str = raw_data.contact_info

    record_to_be_added = {
        "id": id,
        "name": name,
        "address": address,
        "contact_info": contact_info,
    }
    new_customers = models.Customers(**record_to_be_added)
    db.add(new_customers)
    db.commit()
    db.refresh(new_customers)
    customers_inserted_record = new_customers.to_dict()

    res = {
        "customers_inserted_record": customers_inserted_record,
    }
    return res


async def put_customers_id(
    db: Session, id: int, name: str, address: str, contact_info: str
):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.id == id))
    customers_edited_record = query.first()

    if customers_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "address": address,
            "contact_info": contact_info,
        }.items():
            setattr(customers_edited_record, key, value)

        db.commit()
        db.refresh(customers_edited_record)

        customers_edited_record = (
            customers_edited_record.to_dict()
            if hasattr(customers_edited_record, "to_dict")
            else vars(customers_edited_record)
        )
    res = {
        "customers_edited_record": customers_edited_record,
    }
    return res


async def delete_customers_id(db: Session, id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        customers_deleted = record_to_delete.to_dict()
    else:
        customers_deleted = record_to_delete
    res = {
        "customers_deleted": customers_deleted,
    }
    return res


async def get_orders(db: Session):

    query = db.query(models.Orders)

    orders_all = query.all()
    orders_all = (
        [new_data.to_dict() for new_data in orders_all] if orders_all else orders_all
    )
    res = {
        "orders_all": orders_all,
    }
    return res


async def get_orders_id(db: Session, id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.id == id))

    orders_one = query.first()

    orders_one = (
        (orders_one.to_dict() if hasattr(orders_one, "to_dict") else vars(orders_one))
        if orders_one
        else orders_one
    )

    res = {
        "orders_one": orders_one,
    }
    return res


async def put_orders_id(
    db: Session,
    id: int,
    order_date: str,
    shipping_address: str,
    total_cost: str,
    customer_id: int,
):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.id == id))
    orders_edited_record = query.first()

    if orders_edited_record:
        for key, value in {
            "id": id,
            "order_date": order_date,
            "total_cost": total_cost,
            "customer_id": customer_id,
            "shipping_address": shipping_address,
        }.items():
            setattr(orders_edited_record, key, value)

        db.commit()
        db.refresh(orders_edited_record)

        orders_edited_record = (
            orders_edited_record.to_dict()
            if hasattr(orders_edited_record, "to_dict")
            else vars(orders_edited_record)
        )
    res = {
        "orders_edited_record": orders_edited_record,
    }
    return res


async def delete_orders_id(db: Session, id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        orders_deleted = record_to_delete.to_dict()
    else:
        orders_deleted = record_to_delete
    res = {
        "orders_deleted": orders_deleted,
    }
    return res


async def get_order_items(db: Session):

    query = db.query(models.OrderItems)

    order_items_all = query.all()
    order_items_all = (
        [new_data.to_dict() for new_data in order_items_all]
        if order_items_all
        else order_items_all
    )
    res = {
        "order_items_all": order_items_all,
    }
    return res


async def get_order_items_id(db: Session, id: int):

    query = db.query(models.OrderItems)
    query = query.filter(and_(models.OrderItems.id == id))

    order_items_one = query.first()

    order_items_one = (
        (
            order_items_one.to_dict()
            if hasattr(order_items_one, "to_dict")
            else vars(order_items_one)
        )
        if order_items_one
        else order_items_one
    )

    res = {
        "order_items_one": order_items_one,
    }
    return res


async def post_order_items(db: Session, raw_data: schemas.PostOrderItems):
    id: int = raw_data.id
    order_id: int = raw_data.order_id
    product_id: int = raw_data.product_id
    quantity: int = raw_data.quantity

    record_to_be_added = {
        "id": id,
        "order_id": order_id,
        "quantity": quantity,
        "product_id": product_id,
    }
    new_order_items = models.OrderItems(**record_to_be_added)
    db.add(new_order_items)
    db.commit()
    db.refresh(new_order_items)
    order_items_inserted_record = new_order_items.to_dict()

    res = {
        "order_items_inserted_record": order_items_inserted_record,
    }
    return res


async def put_order_items_id(
    db: Session, id: int, order_id: int, product_id: int, quantity: int
):

    query = db.query(models.OrderItems)
    query = query.filter(and_(models.OrderItems.id == id))
    order_items_edited_record = query.first()

    if order_items_edited_record:
        for key, value in {
            "id": id,
            "order_id": order_id,
            "quantity": quantity,
            "product_id": product_id,
        }.items():
            setattr(order_items_edited_record, key, value)

        db.commit()
        db.refresh(order_items_edited_record)

        order_items_edited_record = (
            order_items_edited_record.to_dict()
            if hasattr(order_items_edited_record, "to_dict")
            else vars(order_items_edited_record)
        )
    res = {
        "order_items_edited_record": order_items_edited_record,
    }
    return res


async def delete_order_items_id(db: Session, id: int):

    query = db.query(models.OrderItems)
    query = query.filter(and_(models.OrderItems.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        order_items_deleted = record_to_delete.to_dict()
    else:
        order_items_deleted = record_to_delete
    res = {
        "order_items_deleted": order_items_deleted,
    }
    return res


async def post_products(db: Session, raw_data: schemas.PostProducts):
    id: int = raw_data.id
    name: str = raw_data.name
    description: str = raw_data.description
    price: str = raw_data.price
    image_url: str = raw_data.image_url
    category_id: int = raw_data.category_id

    record_to_be_added = {
        "id": id,
        "name": name,
        "price": price,
        "image_url": image_url,
        "category_id": category_id,
        "description": description,
    }
    new_products = models.Products(**record_to_be_added)
    db.add(new_products)
    db.commit()
    db.refresh(new_products)
    products_inserted_record = new_products.to_dict()

    test = aliased(models.Categories)
    query = db.query(models.Products, test)

    query = query.join(test, and_(models.Products.name == models.Products.name))

    user_details = query.all()
    user_details = (
        [
            {
                "user_details_1": (
                    s1.to_dict() if hasattr(s1, "to_dict") else s1.__dict__
                ),
                "user_details_2": (
                    s2.to_dict() if hasattr(s2, "to_dict") else s2.__dict__
                ),
            }
            for s1, s2 in user_details
        ]
        if user_details
        else user_details
    )

    test1 = aliased(models.Categories)
    query = db.query(models.Products, test1)

    query = query.join(test1, and_(models.Products.description != models.Products.name))

    test1 = query.all()
    test1 = (
        [
            {
                "test1_1": s1.to_dict() if hasattr(s1, "to_dict") else s1.__dict__,
                "test1_2": s2.to_dict() if hasattr(s2, "to_dict") else s2.__dict__,
            }
            for s1, s2 in test1
        ]
        if test1
        else test1
    )
    res = {
        "products_inserted_record": products_inserted_record,
        "user_details": user_details,
        "test1": test1,
    }
    return res
