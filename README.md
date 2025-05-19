 Coffee Shop Domain Modeling

A Python project that models a Coffee Shop domain using object-oriented programming (OOP). Built as part of an assessment to demonstrate understanding of classes, object relationships, data validation, and behavior encapsulation.

Project Structure

coffee_shop/
│
├── customer.py        # Customer class definition
├── coffee.py          # Coffee class definition
├── order.py           # Order class definition
│
├── debug.py           # Manual testing and debugging
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
│
└── README.md           Project overview
```


Domain Overview Entity Relationships

- A Customer can place many Orders
- A Coffee can have many Orders
- An Order belongs to one Customer
 and one Coffee

This results in a many-to-many relationship between `Customer` and `Coffee` via the `Order` class.



Class Breakdown

`Customer`
- Initializes with a validated `name` (1–15 chars)
- `orders()` → returns list of the customer's orders
- `coffees()` → returns unique coffees ordered by the customer
- `create_order(coffee, price)` → adds a new order
- `most_aficionado(coffee)` *(class method)* → customer who spent most on a given coffee

`Coffee`
- Initializes with a validated `name` (≥3 chars)
- `orders()` → returns list of orders for this coffee
- `customers()` → returns unique customers who ordered it
- `num_orders()` → total orders for this coffee
- `average_price()` → average price of all orders

 `Order`
- Initializes with a `Customer`, `Coffee`, and `price` (float between 1.0 and 10.0)
- Ensures data validation and manages association
 Features

- Input validation and exception handling
- OOP design: encapsulation, relationship mapping
- Domain logic modeled without external frameworks
- Clean, testable, and maintainable string


 Testing (Optional)

Testing files are located in the `/tests` directory. To run tests:

```bash
pipenv install pytest
pytest
```

---
 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/ali-b-cell/coffee_shop.git
cd coffee_shop
```

2. Set up the environment:

```bash
pipenv install
pipenv shell
```

3. Run tests or explore via `debug.py`.

---

  Collaboration

To submit for grading, **add your TM as a collaborator** in your GitHub repo settings:

```
Settings → Collaborators → Add by GitHub username
```

---

 Submission

Submit your repository link (use HTTPS):

```
https://github.com/ali-b-cell/coffee_shop
```

---

 Notes

- Project follows PEP 8 style guidelines
- Logic and data validation built from scratch
- No external dependencies required for core functionality

---

Happy Brewing!

