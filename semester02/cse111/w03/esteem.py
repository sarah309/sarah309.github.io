print('''\nThis program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:''')

print('''\nD means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.''')

def add_statements(statement, pos_or_neg):
    print()
    print(statement)
    value = input('Enter D, d, a, or A: ')
    if pos_or_neg == "Negative":
        if value == "D":
            score = 3
        if value == "d":
            score = 2
        if value == "a":
            score = 1
        if value == 'A':
            score = 0
    else:
        if value == 'D':
            score = 0
        if value == "d":
            score = 1
        if value == "a":
            score = 2
        if value == 'A':
            score = 3
    return score

def main():
    total_score = 0
    statements = [['I feel that I am a person of worth, at least on an equal plane with others.', 'Positive'], ['I feel that I have a number of good qualities.', "Positive"], ['All in all, I am inclined to feel that I am a failure.', 'Negative'], ['I am able to do things as well as most other people.', 'Positive'], ['I feel I do not have much to be proud of.', 'Negative'], ['I take a positive attitude toward myself.', 'Positive'], ['On the whole, I am satisfied with myself.', 'Positive'], ['I wish I could have more respect for myself.', 'Negative'], ['I certainly feel useless at times.', 'Negative'], ['At times I think I am no good at all.', 'Negative']]
    for i in range(len(statements)):
        total_score += add_statements(statements[i][0], statements[i][1])
    print()
    print(f'Your score is {total_score}')
    print('A score below 15 may indicate problematic low self-esteem.\n')

if __name__ == "__main__":
    main()