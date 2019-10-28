class InvalidPasswordException(Exception):

    def __init__(self, msg: str):
        self.__msg = msg


def check_password(password: str):
    if len(password) < 8:
        raise InvalidPasswordException("The password must be at least 8 characters long.")


password = input("Please enter your new password: ")
try:
    check_password(password)
except InvalidPasswordException as wpe:
    print(wpe)
else:
    print("You have entered a strong password!")
