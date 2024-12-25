print(
    "Welcome to your escaping from prisons simulation!\n"
    "We are in the Middle Ages, and you are about to be executed in the first morning light. Oh no!"
)

# First stage
firstChoice = input(
    'However, you find a hole in your cell that seems to lead outside. Will you try to escape?\n'
    'Type Y for "yes" and N for "no": '
).strip().lower()

if firstChoice == 'n':
    notEscape = input(
        'Well now. Do you expect the guards to have mercy at the very last minute?\n'
        'Type Y for "yes" and N for "no": '
    ).strip().lower()
    
    if notEscape == 'y':
        print("Too bad! They didn't have any mercy. You died!")
    else:
        print("You are bloody right. You died!")
elif firstChoice == 'y':
    print('Good for you! You are now a fugitive and need to escape the perimeter.')

# Second stage
print(
    'Now, you see yourself in the woods just outside the castle.\n'
    'It is really dark, but you know your way around it very well.'
)

secondChoice = input(
    "Though you escaped, it's just a matter of time before the guards come looking for you.\n"
    "Will you run as fast as you can to get away? You know the drill. Y / N: "
).strip().lower()

if secondChoice == 'y':
    print('They surely heard you running, my guy! You got caught within minutes. You died!')
elif secondChoice == 'n':
    print("Quite the patient guy, are you? But that's nice because no one heard you escaping through the woods.")

# Final stage
print(
    'You walk quite a while and find yourself some options to escape. Your fate depends on which way you are going!'
)

finalPath = input(
    'You can get on a boat and leave the country! Or maybe you can stick to the road ahead and get as far as you can.\n'
    'Or maybe you can climb the mountain just down the road! Or even... go back to the forest.\n'
    'Type your choice! Boat, road, mountain, or forest? '
).strip().lower()

if finalPath == "boat":
    print(
        "You got welcomed into the boat and you are now part of the crew. You're going south, far away from the "
        "kingdom that wants you dead. You get to live!"
    )
elif finalPath == "road":
    print(
        "The guards gave up eventually. You were too far, and they didn't care THAT much.\n"
        "You arrived at the next town and became a baker. You get to live!"
    )
elif finalPath == "mountain":
    print(
        "Really, I don't know what you were thinking. There's no food, wind's aplenty, and it's really, REALLY cold.\n"
        "They never found you. And of course they didn't! You died!"
    )
elif finalPath == "forest":
    print("Why would you? They were here, looking for you, mate! No escape! You died!")
else:
    print("You did not make a choice in time. The guards caught up to you. You got executed as scheduled. You died!")
