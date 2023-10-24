def encode_password(password):
    new_password = ""
    for digit in password:
        new_digit_value = int(digit) + 3
        new_password += str(new_digit_value)
    return new_password


def menu_display():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode \n2. Decode \n3. Quit")
        menu_option = input("\nPlease enter an option: ")
        if menu_option == "1":
            user_password = input("Please enter your password to encode: ")
            stored_password = encode_password(user_password)
            print("Your password has been encoded and stored!\n")
        if menu_option == "2":
            print(f"The encoded password is {stored_password}, and the original password is {user_password}.\n")
        if menu_option == "3":
            break


if __name__ == '__main__':
    menu_display()
