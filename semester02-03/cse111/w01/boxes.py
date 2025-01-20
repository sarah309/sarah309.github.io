import math

manufactured_items = float(input('\n What is the number of manufactured items? '))

items_per_box = (float(input('\n What is the number of items that the user will pack per box? ')))

boxes_needed = manufactured_items / items_per_box
boxes_needed = math.ceil(boxes_needed)

print(f'\n The user will need {boxes_needed} boxes to pack all the manufactured items.\n')