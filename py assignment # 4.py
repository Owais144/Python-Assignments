#Q1
"""
data = [
    {
    'first_name' : 'Owais',
    'last _name' : 'Memon',
    'age' : 20,
    'city' : 'Hyderabad',
}
]
qualification = {
        "qualification" : " "
}

data.append(qualification)
qualification.update({"qualification" : "High academic level"})
print(data)
qualification.popitem()
print(data)
"""
#Q2
"""
cities_info = {

"Karachi" : {
    "Country" : "Pakistan",
    "population" : "14.91 million",
    "fact" : "It is the Sixth largest city in the world by city population"
},
"Las_Vegas":   {"Country" :  "USA",
    "population": "641,676",
      "fact" : "Nuclear bombs were detonated 50 miles from Vegas."


},
"Toronto" :    {"Country" :   "Canada",
        "population": "2.93 million",
        "fact" :"Toronto is the world’s fourth most livable city."

}
}
print(cities_info)
"""
#Q3
"""
while True:
    age =int(input("Enter your age:"))
    if age < 3:
        print("Your ticket is Free")
    elif age < 13 :
        print("Your ticket cost is 10$")
    else :
        print("Your ticket cost is 15$")
"""
#Q4
"""
def favorite_book(title):
    print("One of my fav books is "+title)

favorite_book("Alice in the wonderland")
"""
#Q5
"""
import random
guessestaken= 0
num=random.randint(1,30)
while guessestaken < 3:
    print("Guess the number")
    guess = input()
    guess = int(guess)

    guessestaken =guessestaken + 1

    if guess < num:
        print("Your guess is too low")
    if guess > num:
        print("Your guess is too high")
    if guess == num:
        break

if guess == num:
    guessestaken =str(guessestaken)
    print("You guessed it in" " " +guessestaken+ " " 'guesses')
if guess != num:
    guessestaken =str(guessestaken)
    print("You took all the guesses the number was" " "+str(num))

"""


