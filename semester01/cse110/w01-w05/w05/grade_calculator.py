print()
grade = input('Just out of curiosity...what is your grade percentage? ')
grade = int(grade)
if grade >= 90:
    print('Well done! Your letter grade is A')
elif grade >= 80:
    print('Not too shabby...your letter grade is B')
elif grade >= 70:
    print("You're cutting it close...your letter grade is C")
elif grade >= 60:
    print('Your letter grade is D. This is gonna take some work to bring up, but I think you still have a chance.')
elif grade <= 50:
    print("I don't quite know how to tell you this, but...your letter grade is F")
if grade >= 70:
    print('Congrats! You passed the course!')
if grade < 70:
    print('Might I suggest a tutor?')
