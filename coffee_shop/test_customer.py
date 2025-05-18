import pytest
from customer import Customer

def test_customer_name_valid():
    c = Customer("Bob")
    assert c.name == "Bob"

def test_customer_name_invalid():
    with pytest.raises(ValueError):
        Customer("")

        