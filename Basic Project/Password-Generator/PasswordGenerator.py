import random

# Password generator method
#it is going to generate a password with the length obtained with alphabets and numbers

def generate_password(pw_lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in pw_lengths:
        password = ""
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]

        password = replace_number(password)
        password = replace_uppercase_letter(password)

        passwords.append(password)

    return passwords

#Its going to replace the numbers if they are already in other passwords

def replace_number(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword

#Its going to replace the lowercase letter to uppercase letters
def replace_uppercase_letter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword

#main method
def main():
    num_pass = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(num_pass) + " passwords")

    password_lengths = []

    print("Minimum length of password should be 3")

    for i in range(num_pass):
        length = int(input("Enter the length of Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        password_lengths.append(length)

    passwords = generate_password(password_lengths)

    for i, password in enumerate(passwords):
        print("Password #" + str(i + 1) + " = " + password)

# Main
if __name__ == "__main__":
    main()