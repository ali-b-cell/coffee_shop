class Customer:
  def __init__(self, name):
      self.name  = name
      self._orders = [] 

  @property
  def name(self):
     return self._name 

  @name.setter
  def name(self, value):
     if isinstance(value, str) and 1 <= len(value) <= 15:
        self._name = value
     else: 
        raise ValueError("Customer name must be a string between 1 and 15 characters." )
     
  def orders(self):
     return self._orders
  
  def coffee(self):
     return list(set(order.coffee for order in self._orders))
  
  def create_order(self, coffee, price):
     from order import Order
     return Order(self, coffee, price)
  
  @classmethod
  def most_aficionado(cls, coffee):
      max_spent = 0
      top_customer = None
      for order in coffee.orders():
          total = sum(o.price for o in order.customer.orders() if o.coffee == coffee)
          if total > max_spent:
             max_spent = total
             top_customer = order.customer
      return top_customer       
        
      
        