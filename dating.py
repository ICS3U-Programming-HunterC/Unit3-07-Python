#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 6, 2022
# the user enters their age and then the program tells
# you if you can date their grandchild.


def main():

    # get the user's age as a string
    age_as_string = input("Enter your age: ")
    print("")

    # switch the age into an int and then check if it is a number and if
    # it is correct or not
    try:
        age_as_number = int(age_as_string)
        if (age_as_number < 40) and (age_as_number > 25):
            print("You are the perfect age to date our grandchild! :)")
        elif age_as_number > 40:
            print("You are too old to date our grandchild :(")
        elif age_as_number < 25:
            print("You are too young to date our grandchild :(")
    except Exception:
        print("That is not an age!! try again!!")


if __name__ == "__main__":
    main()
