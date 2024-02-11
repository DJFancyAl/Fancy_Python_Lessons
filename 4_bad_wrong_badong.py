"""

Chicken go "Cluck Cluck" cow goes "Moooo". I've got a challenge for youuuu. This one is simple! Right?

First of all - add a movie to the movies dictionary, but don't add it directly to the movies dictionary. All 
of your code must be below the comment line.
Then all you have to do is iterate through movies and for each move print 
"The best line in <<movie>> is <<quote>>."

Hints:
* Remember how to assign dictionary key, value pairs.
* This will be a bit trickier...we're used to iterating lists, but "movies" is a dictionary.
* Take your time studying the "movies" dictionary to understand what's going on.

"""

movies = {
    "Kung Pow": [
        2002,
        "The name is Betty you son of a pig."
    ],
    "Hot Rod": [
        2007,
        "Funky Fresh"
    ],
    "Strange Wilderness": [
        2008,
        "Let's go find us some pygmy people."
    ]
}

# Write your code below this line.

def add_movie(title, year, quote):
    movies[title] = [year, quote]

add_movie("Joe Dirt", 2001, "Life's a garden, dig it.")

for movie, (year, quote) in movies.items():
    print(f"The best line in {movie} is '{quote}'.")
    print(" ")