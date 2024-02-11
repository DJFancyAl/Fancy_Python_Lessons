'''
In this challenge you'll play the role of R.J...we need to announce the players by their position!

We've saved our data in the "sabres" list - a list of lists...iterate through the Sabres list and print out an announcement.
If the player is a defensemen print something like: "#6 on defense...is Johnson".
If the play is a forward print something like: "Playing forward: #21 is Okposo".
Also add an empty line between each announcement to space things out.

Hints:
* Remember what a list index is
* Notice that there are 3 types of forwards, but they're all forwards. Really think about how you'll set up your conditionals.

'''

sabres = [
    ['Johnson', 33, 'D'],
    ['Benson', 9, 'LW'],
    ['Cozens', 24, 'C'],
    ['Dahlin', 26, 'D'],
    ['Girgensons', 28, 'LW'],
    ['Johnson', 6, 'D'],
    ['Greenway', 12, 'LW'],
    ['Powers', 25, 'D'],
    ['Krebs', 19, 'C'],
    ['Clifton', 75, 'D'],
    ['Mittelstadt', 37, 'C'],
    ['Okposo', 21, 'RW'],
    ['Jokiharju', 10, 'D'],
    ['Peterka', 77, 'RW'],
    ['Quinn', 22, 'RW'],
    ['Skinner', 53, 'LW'],
    ['Thompson', 72, 'C'],
    ['Tuch', 89, 'RW'],
    ['Samuelsson', 23, 'D']
]

# Write your code below this line.
for player in sabres:
    if player[2] == "D":
        print(f"#{player[1]} on defense...is {player[0]}!\n")
    else:
        print(f"Playing forward: #{player[1]} is {player[0]}!\n")