def menu_display():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode \n2. Decode \n3. Quit")
        print("\nPlease enter an option: ")
    menu_option = input("Please enter an option: ")
    if menu_option == "1":
        user_password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
    if menu_option == "2":
        for digit in user_password:
            digit += 3
        print(f'The encoded password is {user_password}, and the original password is {}.")
    if menu_option == "3":
        break

if __name__ == '__main__':
    menu_display()
