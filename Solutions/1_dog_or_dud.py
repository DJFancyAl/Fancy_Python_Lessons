"""

Exercise #1 - Dog or Dud?
Use iteration on the "dogs" list below to tell us what type of dog it is. If the dog's name is less than 5 characters long, then print a statement saying the dog is a lil dud ("Lola is a lil dud" for example). If the dog's name is 5 or more characters long, then print a statement saying the dog is a BIG DOG ("Chubbs is a BIG DOG for example).

Hints:
* You need to determine the length of each name. Maybe a built-in function?
* A good opportunity to use f-strings?

"""

dogs = ['Chubbs', 'Pucky', 'Bode', 'Lola', 'Rosie', 'Newman', 'Sooley', 'Olga']

# Write your code beneath this line.

for dog in dogs:
    if len(dog) < 5:
        print(f"{dog} is a lil dud")
    else:
        print(f"{dog} is a BIG DOG")
