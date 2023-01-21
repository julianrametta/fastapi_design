from fastapi import APIRouter

from src.operations.customers import (
    CustomerCreateData,
    CustomerUpdateData,
    create_customer,
    read_all_customers,
    read_customer,
    update_customer,
)

from src.db.models import DBCustomer
from src.db.db_interface import DBInterface

router = APIRouter()


@router.get("/customers")
def api_read_all_customers():
    customer_interface = DBInterface(DBCustomer)
    return read_all_customers(customer_interface)


@router.get("/customer/{customer_id}")
def api_read_customer(customer_id: int):
    customer_interface = DBInterface(DBCustomer)
    return read_customer(customer_id, customer_interface)


@router.post("/customer")
def api_add_customer(new_customer: CustomerCreateData):
    customer_interface = DBInterface(DBCustomer)
    return create_customer(new_customer, customer_interface)


@router.post("/customer/{customer_id}")
def api_update_customer(customer_id: int, customer: CustomerUpdateData):
    customer_interface = DBInterface(DBCustomer)
    return update_customer(customer_id, customer, customer_interface)
