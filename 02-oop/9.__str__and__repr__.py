

class Car :
   def __init__(self, name:str, price:int):
      self.name = name
      self.price = price

    # string representation what ever we want
   def __str__(self):
      return f"car name -> {self.name} \ncar price -> {self.price}"

    # something represenation that important to developer
   def __repr__(self):
      return f"Car(name={self.name},price={self.price})"

car = Car('bmw', 100)
print(car)
print(car.__repr__())
