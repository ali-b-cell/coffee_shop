import pytest
from customer import Customer 
from coffee import Coffee
from order import Order

def test_order_valid_creation():
    customer = Customer("Eva")
    coffee = Coffee("Cappuccino")
    order = Order(customer, coffee, 5.0)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_invalid_price_low():
    customer = Customer("Finn")
    coffee = Coffee("Mocha")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)

def test_order_invalid_customer_class_type():
    coffee = Coffee("Mocha")
    with pytest.raises(ValueError):
        Order(Customer, coffee, 3.0)


def test_order_invalid_customer_type():
    coffee = Coffee("Mocha")
    with pytest.raises(ValueError):
        Order("NotACustomer", coffee, 3.0)

def test_order_invalid_coffee_type():
    customer = Customer("Henry")
    with pytest.raises(ValueError):
        Order(customer,  "NotACoffee", 3.0)


              

 