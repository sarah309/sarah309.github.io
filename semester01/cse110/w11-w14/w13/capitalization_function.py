def display_regular(message):
    return message

def display_uppercase(message):
    return message.upper()

def display_lowercase(message):
    return message.lower()

message = input("\nWhat is your message? ")

print()

message_regular = display_regular(message)
message_uppercase = display_uppercase(message)
message_lowercase = display_lowercase(message)

print(message_regular)
print(message_uppercase)
print(message_lowercase)

print()