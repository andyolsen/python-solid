import winsound


class Root:
    def __init__(self):
        print("Done Root initialization")


class Logger(Root):
    def __init__(self):
        super().__init__()
        print("Done Logger initialization")

    def log(self, msg):
        print(msg)


class Beeper(Root):
    def __init__(self):
        super().__init__()
        print("Done Beeper initialization")

    def beep(self, duration):
        winsound.Beep(2500, duration)


class Alerter(Logger, Beeper):
    def __init__(self):
        super().__init__()
        print("Done Alerter initialization")

    def doShortAlert(self, msg):
        super().log(msg)
        super().beep(250)

    def doMediumAlert(self, msg):
        super().log(msg)
        super().beep(1000)

    def doLongAlert(self, msg):
        super().log(msg)
        super().beep(2500)


# Client code.
print("Method resolution order for Alerter:")
print(Alerter.mro())

print("\nMRO decides which method to call:")
alerter = Alerter()