class Fruit :
     def __init__(self, name:str):
       self.__name  = name;

     # getter define for  private attribute
     @property
     def name(self):
      return self.__name

    # setter, shoud use getter function name for setter
     @name.setter
     def name(self,value:str):
         self.__name =value




mango :Fruit = Fruit('mango sri lanka')

# can't access beacuse __name is private
print(mango.name)

#setter
mango.name = 'mango changed'
print(mango.name)
