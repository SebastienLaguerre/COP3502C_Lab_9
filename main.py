def menu():
    print("Menu")
    print()
    print("-------------")
    print()
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    print()

if __name__ == "__main__":
    menu()
    option = int(input("Please enter an option: "))
    encoded_string = " "
    if option == 1:
        password = input("Please enter your password to encode: ")
        for i in password:
            if i == "0":
                encoded_string += "3"
            if i == "1":
                encoded_string += "4"
            if i == "2":
                encoded_string += "5"
            if i == "3":
                encoded_string += "6"
            if i == "4":
                encoded_string += "7"
            if i == "5":
                encoded_string += "8"
            if i == "6":
                encoded_string += "9"
            if i == "7":
                encoded_string += "0"
            if i == "8":
                encoded_string += "1"
            if i == "9":
                encoded_string += "2"
        print(encoded_string)
        print("Your password has been encoded and stored!")

    if option == 2:
        # i know how to do this but this is easier lol
        # seamus added this functionality
        print(f"The encoded password is {encoded_string}, and the original password is {password}")
    if option == 3:
        # seamus also added this functionality
        break

if __name__ == "__main__":
        main()


