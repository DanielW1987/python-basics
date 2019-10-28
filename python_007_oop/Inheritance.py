class BMW:

    def __int__(self, maker: str, model: str, year: int):
        self.__maker = maker
        self.__model = model
        self.__year = year

    def start(self) -> None:
        print("Starting the car")

    def stop(self) -> None:
        print("Stopping the car")


class ThreeSeries(BMW):

    def __init__(self, maker: str, model: str, year: int, cruise_control_enabled: bool):
        super().__int__(maker, model, year) # invoking super constructor
        self.__cruise_control_enabled = cruise_control_enabled

    def start(self) -> None:
        super().start()
        print("Button start")


class FiveSeries(BMW):

    def __init__(self, maker: str, model: str, year: int, parking_assist_enabled: bool):
        super().__int__(maker, model, year) # invoking super constructor
        self.__parking_assist_enabled = parking_assist_enabled


three_series: BMW = ThreeSeries("BMW", "328i", 2018, True)
three_series.start()
three_series.stop()
