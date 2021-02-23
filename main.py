from lib.Sonic.Echo import Echo
from lib.RainbowHAT.RainbowHAT import RainbowHAT


class App:
    def __init__(self, name="Application Name"):
        self.setEcho()
        self.setRainbowHAT()
        print(name)

    def setEcho(self):
        self.echo = Echo()

    def setRainbowHAT(self):
        self.hat = RainbowHAT()


def main():
    App("RasPi with RainbowHAT")


if __name__ == "__main__":
    main()
