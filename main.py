# Write a story with some words missing
story = """
Rose are {}
Violetes are {}
sugar is {}
And so are you
"""
# Ask the uses to provide the missing words
colour1 = input("Give flower colour: ")
colour2 = input("Give a plant colour: ")
ad = input("And an adjective: ")

# Display the final story
print(story.format(colour1, colour2, ad))


