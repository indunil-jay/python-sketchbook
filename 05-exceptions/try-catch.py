user_input = "aka"


try:
    number = float(user_input)
    print(number)
except Exception as e:
    print(e)

# else reach if try block is success
else:
    print('successfully executed code.')

# finally reach regardless of no matter what happen always runs
finally:
    print("end")
