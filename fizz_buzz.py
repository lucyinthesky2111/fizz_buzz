
# Number divisible by 3 = "Fizz"
# Number divisible by 5 = "Buzz"
# Number divisible by 3 and 5 = "FizzBuzz"
# Otherwise say the original number 

num = int(input("Enter a number: "))

# Modulus operator divides a number and gives the remainder
# As we are checking if numbers divide exactly by 3 and 5, we meed there to be no remainder
# after the division i.e. the modulus needs to be zero
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("FizzBuzz")