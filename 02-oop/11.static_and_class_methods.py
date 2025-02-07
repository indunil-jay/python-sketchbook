class Calculator :

    def __init__(self,name:str):
        self.name = name
   #instance method
    def description(self):
        return f"{self.name} is calculator."

    # static methods are basically utility function that is  not dependent on class itself , no relations
    @staticmethod
    def add(a:int,b:int):
        return a+b

    # classmethod is special method, it has access to the class it self , not the instane,so instacne variable
    # cannot access @classmethod, but can access class variables and other method, usualy this kind of method
    # help for add mutation to existsings ones
    @classmethod
    def classWithVersion(cls,version:str,name:str):
      return cls(f"{name}:({version})")


calculator  = Calculator('Mathematic PG970X')

print(Calculator.add(2,3))


cal = Calculator.classWithVersion('2.0','cal')
