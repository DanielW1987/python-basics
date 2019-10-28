from abc import abstractmethod, ABC


# In Python, an interface is a class that has only abstract methods
class Drivable(ABC):

    @abstractmethod
    def drive(self) -> None:
        pass


class BMW(ABC, Drivable):

    def __int__(self, maker: str, model: str, year: int):
        self.__maker = maker
        self.__model = model
        self.__year = year

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class ThreeSeries(BMW):

    def __init__(self, maker: str, model: str, year: int, cruise_control_enabled: bool):
        super().__int__(maker, model, year) # invoking super constructor
        self.__cruise_control_enabled = cruise_control_enabled

    def start(self) -> None:
        print("Three series start")

    def stop(self) -> None:
        print("Three series stop")

    def drive(self) -> None:
        print("Three series is being driven")


class FiveSeries(BMW):

    def __init__(self, maker: str, model: str, year: int, parking_assist_enabled: bool):
        super().__int__(maker, model, year) # invoking super constructor
        self.__parking_assist_enabled = parking_assist_enabled

    def start(self) -> None:
        print("Five series start")

    def stop(self) -> None:
        print("Five series stop")

    def drive(self) -> None:
        print("Five Series is being driven")


three_series: BMW = ThreeSeries("BMW", "328i", 2018, True)
three_series.start()
three_series.stop()
