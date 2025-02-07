# What is polymorphism?

# While inheritance is the most unique trait of object-oriented languages, polymorphism is probably the most powerful.
#  Polymorphism is the ability of a variable, function or object to take on multiple forms.
    #  "poly"="many"
    #  "morph"="form".

class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims

# The Dragon and Kraken child classes are overriding the behavior of their parent class's move() method.

# Polymorphism Review

# Take a look at the Greek roots of the word "polymorphism".

#     "poly" means "many".
#     "morph" means "to change" or "form".

# Polymorphism in programming is the ability to present the same interface (function or method signatures) for many different underlying forms (data types).

# A classic example is a Shape class that Rectangle, Circle, and Triangle can inherit from. With polymorphism,
# each of these classes will have different underlying data. The circle needs its center point coordinates and radius.
# The rectangle needs two coordinates for the top left and bottom right corners. The triangle needs coordinates for the corners.

# By making each class responsible for its data and its code, you can achieve polymorphism. In the shapes example,
#  each class would have its own draw_shape() method. This allows the code that uses the different shapes to be simple and easy,
# and more importantly, it can treat shapes as the same even though they are different. It hides the complexities of the difference behind a clean abstraction.

# shapes = [Circle(5, 5, 10), Rectangle(1, 3, 5, 6)]
# for shape in shapes:
#     print(shape.draw_shape())

# This is in contrast to the functional way of doing things where you would have had separate functions that have different function signatures,
# like draw_rectangle(x1, y1, x2, y2) and draw_circle(x, y, radius).

# Wait, what is a "function signature"?

# A function signature (or method signature) includes the name, inputs, and outputs of a function or method. For example, hit_by_fire in the Human and Archer classes have identical signatures.

# class Human:
#     def hit_by_fire(self):
#         self.health -= 5
#         return self.health

# class Archer:
#     def hit_by_fire(self):
#         self.health -= 10
#         return self.health

# Both methods have the same name, take 0 inputs, and return integers. If any of those things were different, they would have different function signatures.

# Here is an example of different signatures:

# class Human:
#     def hit_by_fire(self):
#         self.health -= 5
#         return self.health

# class Archer:
#     def hit_by_fire(self, dmg):
#         self.health -= dmg
#         return self.health

# The Archer class's hit_by_fire method takes an input, dmg, which is used to calculate the new health.
# This is a different signature than the Human class's hit_by_fire method, which takes no inputs. Calling two methods with the same signature should look the same to the caller.

# # same inputs (none)
# # same name
# # same outputs (a single integer)
# health = sam.hit_by_fire()
# health = archer.hit_by_fire()

# When overriding methods, use the same function signature

# If you change the function signature of a parent class when overriding a method, it could be a disaster.
# The whole point of overriding a method is so that the caller of your code doesn't have to worry about what different things are going on inside the methods of different object types.

##########################################
# Operator Overloading

# Another kind of built-in polymorphism in Python is the ability to override how an operator works. For example, the + operator works for built-in types like integers and strings.

print(3 + 4)
# prints "7"

print("three " + "four")
# prints "three four"

# Custom classes on the other hand don't have any built-in support for those operators:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
p2 = Point(2, 3)
# p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

# However, we can add our own support! If we create an __add__(self, other) method on our class,
# the Python interpreter will use it when instances of the class are being added with the + operator. Here's an example:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)

# Now, when p1 + p2 is executed, under the hood the Python interpreter just calls p1.__add__(p2).


# Operator Overload Review

# As we discussed in the last assignment, operator overloading is the practice of defining custom behavior for standard Python operators.
#  Here's a list of how the operators translate into method names.


# +-----------------------+------------+------------  +
# |       Operation       |  Operator  |   Method     |
# +-----------------------+------------+------------  +
# | Addition              |     +      |  __add__     |
# | Subtraction           |     -      |  __sub__     |
# | Multiplication        |     *      |  __mul__     |
# | Power                 |    **      |  __pow__     |
# | Division              |     /      |  __truediv__ |
# | Floor Division        |    //      |  __floordiv__|
# | Remainder (modulo)    |     %      |  __mod__     |
# | Bitwise Left Shift    |    <<      |  __lshift__  |
# | Bitwise Right Shift   |    >>      |  __rshift__  |
# | Bitwise AND           |     &      |  __and__     |
# | Bitwise OR            |     |      |  __or__      |
# | Bitwise XOR           |     ^      |  __xor__     |
# | Bitwise NOT           |     ~      |  __invert__  |
# +-----------------------+------------+------------+

#  The __str__ method (short for "string") lets us do just that. It takes no inputs but
#  returns a string that will be printed to the console when someone passes an instance of the class to Python's print() function.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

p1 = Point(4, 5)
print(p1)
# prints "(4,5)"
