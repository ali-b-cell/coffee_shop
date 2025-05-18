from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Joy")
c2 = Customer("Ben")
coffee1 = Coffee("Mocha")
coffee2 = Coffee("Espresso")

c1.create_order(coffee1, 3.5)
c1.create_order(coffee2, 4.0)
c2.create_order(coffee1, 4.5)

print(Coffee("Mocha").average_price())
