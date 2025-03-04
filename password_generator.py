import random, string
letters = string.ascii_letters
numbers = string.digits
special_characters = "!@#$%^&*()_+"
print(f"you'r password is: {random.choice(letters)}{random.choice(numbers)}{random.choice(special_characters)}")
password=("".join(random.choices(letters + numbers + special_characters, k=7)))
print(f"you'r password is: {password}")
