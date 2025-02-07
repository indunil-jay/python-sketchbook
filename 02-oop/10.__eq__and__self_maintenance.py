

class Car :
   def __init__(self, name:str, price:int):
      self.name = name
      self.price = price

   # check equality of two distinict instance
   def __eq__(self, value):

      return self.__dict__ == value.__dict__

  # inbuild method can only be use inside class, no outside interaction
   def __self_maintenance(self):
      print('this can accessiable within the class')

   def doSomthing(self):
        self.__self_maintenance()




car1 = Car('bmw', 100)
car2 = Car('bmw', 100)

print(car1==car2)

# car1.__self_maintenance() error
car1.doSomthing()
