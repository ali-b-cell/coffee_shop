class Coffee:
  def __init__(self, name):
    self._orders = []
    self.name = name

  @property
  def name(self):
      return self._name
    
  @name.setter
  def name(self, value):
      if isinstance(value, str) and len(value) >= 3:
          self._name = value
      else:
          raise ValueError("Coffee name must be at least 3 characters long,")
      
  def orders(self):
   return self._orders
  
  def customers(self):
    return list(set(order.customer for order in self._orders))
  
  def num_orders(self):
    return len(self._orders)
  
  def average_price(self):
    if not self._orders:
      return 0
    return sum(order.price for order in self._orders) / len(self._orders)
  
       


    