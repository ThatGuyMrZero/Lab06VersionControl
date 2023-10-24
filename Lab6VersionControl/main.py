# Michael Zero

def password_encoder(password):
    encoded_password = ""
    for digit in password:
        if digit.isdigit():
            encoded_digit = (int(digit) + 3) % 10
            encoded_password += str(encoded_digit)
        return encoded_password


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = int(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif option == 2:
            pass
        elif option == 3:
            break
        else:
            print("Invalid menu option")
