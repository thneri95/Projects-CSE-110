"Activity 01 CSE-110"
"Author: Tiago Borges"

# Below we have the words that we need to programing and make the "Variables"
# Ask the user for inputs

print("Please enter the following words to complete the story:")
adjective = input("Adjective: ")
animal = input("Animal: ")
verb1 = input("Verb : ")
exclamation = input("Exclamation: ").capitalize()  # Automatically capitalize the exclamation
verb2 = input("Verb : ")
verb3 = input("Verb : ")

# Now i´ll gonna to create our program code, let´s do it! 
# Story template with user inputs
story = f"""
The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family.
"""

# Display the completed story
print("\nYour story is:")
print(story)

# Thanks for this lesson! I've learned a lot.

