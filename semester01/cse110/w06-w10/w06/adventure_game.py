print()
first_choice = input("You are caught in a blizzard after a car tire is punctured by a nail while enroute to your parents’ house. You see a small log CABIN with lights on not too far off. You also see a TRUCK’s headlights approaching. Which do you turn to for help? ")
print()
if first_choice.lower() == "cabin":
    second_choice = input("You reach the cabin and knock. Nobody answers. Do you KNOCK again, BREAK in, or RETURN to your car? ")
    print()
    if second_choice.lower() == "knock":
        third_choice = input("A little old lady answers the door, and you get blasted by both a wave of heat and the aroma of freshly baked oatmeal raisin cookies. She invites you in and offers you a platter of vibrant green kale. Do you ACCEPT the kale or DEMAND a plate of cookies? ")
        print()
        if third_choice.lower() == "accept":
            print("This sweet little old lady watches you take every bite and then gives you two oatmeal raisin cookies to reward you for eating all your veggies. She invites you to stay as long as you need. You never make it to your parents’ house and live out the rest of your days eating leafy greens and oatmeal raisin cookies.")
        elif third_choice.lower() == "demand":
            print("You never make it to your parents’ house, but spend the rest of your days in the naughty chair.")
        else:
            invalid = input("Invalid response.")
    elif second_choice.lower() == "break":
        third_choice = input("You find a key under the Welcome mat and unlock the door. You see a little old lady hobbling toward the door at a cool 1 mph. She stops dead in her tracks when she sees you. Do you APOLOGIZE and explain your situation, or RUN out the door and never look back? ")
        print()
        if third_choice.lower() == "apologize":
            print("The little old lady mistakes you for her grandson and you spend the rest of the night drinking prune juice and telling her what her great grandchildren are up to these days.")
        elif third_choice.lower() == "run":
            print("You get lost in the blizzard and can’t find your car. Fortunately, you stumble upon a cave that is stocked with enough potato chips, apple fritters, green bean casseroles, bean burritos, and carrot cupcakes to get you comfortably through retirement.")
        else:
            invalid = input("Invalid response.")
    elif second_choice.lower() == "return":
        third_choice = input("Defeated, you head back to your car. Just when it looks like you’ve run out of all options, a pack of wolves appears out of nowhere. They head into the nearby woods and stop, looking back, waiting for you. Do you FOLLOW them or politely DECLINE? ")
        print()
        if third_choice.lower() == "follow":
            print("So…they adopt you into their pack and you spend the remainder of your days learning how to be a wolf.")
        elif third_choice.lower() == "decline":
            print("The pack leaves you stranded and you are left to survive the raging blizzard on your own…good luck.")
        else:
            invalid = input("Invalid response.")
    else:
        invalid = input("Invalid response.")
elif first_choice.lower() == "truck":
    second_choice = input("You wave for help from the truck and the driver pulls over. A man gets out and offers to DRIVE you to the nearest town or to REPLACE your punctured tire with his spare. Which do you choose? ")
    print()
    if second_choice.lower() == "drive":
        third_choice = input("It’s about a 15 minute drive to the nearest town. The truck driver finds you a motel and you part ways. You get a room and, just before collapsing into bed, you notice a large wet stain on the sheets. Do you request a new ROOM, sleep on top of the COMFORTER, or sleep on the COUCH? ")
        print()
        if third_choice.lower() == "room":
            print("They kindly grant you a new room, which also happens to be a custodians closet, which has many larger and wetter stains in it.")
        elif third_choice.lower() == "comforter":
            print("You nearly turn into a block of ice during the night. Thankfully, you can get a spare tire the next day and don’t need to spend another night there.")
        elif third_choice.lower() == "couch":
            print("You get such a bad crick in your neck that your doctor diagnosed it as dislocated. Your mom spoon feeds you homemade vegetable soup for the next three months while you recover.")
    elif second_choice.lower() == "replace":
        third_choice = input("It takes about 5 minutes for this guy to change the tire. You head your separate ways, and you reach your parents’ house a few hours later. They want to hear everything but you are exhausted. Do you share the long STORY of your travels or head straight to BED? ")
        print()
        if third_choice.lower() == "story":
            print("You fall asleep midway through. Mom prepares your favorite blueberry pancakes the next morning and you enjoy a picture-perfect visit with your family.")
        elif third_choice == "bed":
            print("Offended, Mom refuses to tuck you in and Dad grounds you for two months from electronics. But the next morning, after you tell them the events of the night before, Mom forgives you and Dad ungrounds you.")
    else:
        invalid = input("Invalid response.")
else:
    invalid = input("Invalid response.")
print()