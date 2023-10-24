# Michael Zero

def password_encoder(password):
    encoded_password = ""
    for digit in password:
        if digit.isdigit():
            encoded_digit = (int(digit) + 3) % 10
            encoded_password += str(encoded_digit)

    return encoded_password


def password_decoder(encoded):
    decoded_password = ""
    pswrd_list = [int(i) for i in encoded]
    for i in pswrd_list:
        if i == 0:
            i = 3
        elif i == 1:
            i = 13
        elif i == 2:
            i = 12
        num = i - 3
        decoded_password += str(num)
    return decoded_password


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
            password = input("Please enter your password to encode: ")
            encoded_password = password_encoder(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            password = password_decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")
        elif option == 3:
            break
        else:
            print("Invalid menu option")
