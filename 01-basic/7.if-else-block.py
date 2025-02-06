# if statements
# It's often useful to only execute code if a certain condition is met:

bob_score=5
bill_score=4

if bob_score > bill_score:
	print("Bob Wins!")

print("Game Complete")

# Remember, you can use the == operator to check if two values are equal. For example:

# else if
score=40
high_score=80
second_highest_score=60
third_highest_score=35

if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")


    # Here are some basic rules with if/else blocks.

    # You can't have an elif or an else without an if
    # You can have an else without an el


#### Boolean logic ##########

# Boolean logic refers to logic dealing with boolean (True or False) values
def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100

def is_car_cool(speed, is_electric):
    return speed > 200 or is_electric
