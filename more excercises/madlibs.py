# write a story with some words missing

story = """ 
Roses are {}
Violets are {}
Sugar is {}
and so are you
"""

# ask user to provide missing words

color = input("Give me a color:\n")
color2 = input("Give me another color:\n")
adjective = input("And an adjective:\n")


# Display the final story
print(story.format(color.lower(), color2.lower(), adjective.lower()))
