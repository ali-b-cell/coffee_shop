import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_valid():
    c = Coffee("Espresso")
    assert c.name == "Espresso"

def test_coffee_name_invalid():
    with pytest.raises(ValueError):
        Coffee("Ab")

def test_coffee_orders_and_customers():
    coffee = Coffee("Mocha")
    customer1 = Customer("lucy")
    customer2 = Customer("Bob")

    o1 = Order(customer1, coffee, 3.0)
    o2 = Order(customer2, coffee, 4.0)

    assert len(coffee.orders()) == 2
    assert set(coffee.customers()) == {customer1, customer2}

def test_num_orders():
    coffee = Coffee("Mocha")
    customer = Customer("Charlie")

    Order(customer, coffee, 3.0)
    Order(customer, coffee, 3.5)

    assert coffee.num_orders() == 2

def test_average_price():
    coffee = Coffee("Americano")
    customer = Customer("Dana")

    Order(customer, coffee, 2.0)
    Order(customer, coffee, 4.0)

    assert coffee.average_price() == 3.0

def test_average_price_zero_orders():
    coffee = Coffee("EmptyCup") 
    assert coffee.average_price() == 0   

    

