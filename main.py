# main file for the password generator
# imports
import sys
import random
import string


class Main:
    def __init__(self, PASS_LENGTH):
        self.PASS_LENGTH = PASS_LENGTH
        self.password = ""

    def generate_password(self):
        # method to generate a random password

        # store characters to generate password
        symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
        store_characters = []
        for symbol in symbols:
            store_characters.append(symbol)

        # generate a random password
        counting = 0

        # try to check if the password length is not exceeding the number of characters
        try:
            chars = random.sample(store_characters, k=PASS_LENGTH)
        except ValueError:
            print("Password length cannot exceed more than 62 characters")
            sys.exit()

        # main loop
        for char in chars:
            # check if the password length is equal to counting
            if PASS_LENGTH == counting:
                break

            # get the twenty percent of the password length
            twenty_percent = round(0.20 * PASS_LENGTH)
            strong_chars = ["!", "@", "#", "$", "%", "&", "?"]

            # add strong characters to the password
            if counting % twenty_percent == 0:
                self.password += random.choice(strong_chars)
            else:
                self.password += char

            counting += 1

        print(self.password)

    def store_passwords(self, SITE_NAME, FILE_NAME="passwords.txt"):
        # method to store passwords in a plain text file

        with open(FILE_NAME, "a") as file_obj:
            to_write = f"{SITE_NAME} - {self.password}\n"
            file_obj.write(to_write)

        print(f"Your password is: {self.password}")


# get the length of password
try:
    PASS_LENGTH = int(input("\nEnter the length of the password -> "))
except ValueError:
    print("Please enter a number not a string")
    sys.exit()

# get the name of the site to which the user is creating password for
SITE_NAME = input("Enter the name of the website which you want to create password for -> ")

# show the password
password = Main(PASS_LENGTH)
password.generate_password()
password.store_passwords(SITE_NAME)
