"""

Okay pal. It's an election year, so that means it's time for Bidenomics! The country is doing gReAt, but we're gonna need some mail in ballots anyways. We just need a way to calculate how many "mail-ins" we'll need to put China Joe over the top.

Create a script that accepts a number as user input. Then use a function called "protect_democracy" to multiply the user's input by 120%. Then add that value to the total_votes variable. Lastly, when the total votes exceeds 100 million - print the message "Got em Jack!" and end the script.

For example, I should be able to input:
input(25000000)
input(20000000)
input(5000000)
input(10000000)
input(30000000)
input(15000000)
Got em Jack!

Hints:
* I've already created the total_votes variable. You've gotta add to it.
* Remember how function parameters and returns work.
* You don't know how many inputs the user will provide, but you want to keep the app running. If only there was a loop for that...

"""

total_votes = 0

# Create the protect_democracy function below this line
def protect_democracy(votes):
    boosted = float(votes) * 1.2
    return boosted

# Write the rest of your script below this line
while total_votes < 100000000:
    votes = input("Enter number of votes: ")
    total_votes += int(protect_democracy(votes))

    print(f"{votes} votes added!!\n{total_votes} votes counted so far!!\n")

print("Got em jACKKKKKKKKKK")