import winsound

class Logger:

    def __init__(self):
        print("Logger __init__ called")

    def log(self, msg):
        print(msg)


class Beeper:

    def __init__(self):
        print("Beeper __init__ called")

    def beep(self, duration):
        winsound.Beep(2500, duration)


class Alerter(Logger, Beeper):

    def __init__(self):
        print("Alerter __init__ called, about to call Logger's and Beeper's __init__ too...")

        # Can call superclass initializers, manually by classname:
        # Logger.__init__(self)
        # Beeper.__init__(self)

        # Or can call superclass initializers, relying on the method resolution rules (mro).
        super().__init__()               # This will call the __init__() method immediately next in the mro (i.e. Logger).
        super(Logger, self).__init__()   # This will call all __init__() methods after Logger in the mro.

        print("Alerter __init__ all done dude")

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

print("\nCreate Alerter instance:")
alerter = Alerter()