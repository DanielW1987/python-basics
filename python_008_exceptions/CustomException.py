class OverTheLimitException(Exception):

    def __init__(self, msg: str):
        self.__msg = msg


def withdrawl(amount: int) -> None:
    if amount > 500:
        raise OverTheLimitException("You can not withdraw more than 500")


withdrawl(501)
