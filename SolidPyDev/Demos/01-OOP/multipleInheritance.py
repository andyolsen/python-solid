import winsound

class Logger:
    def log(self, msg):
        print(msg)


class Beeper:
    def beep(self, duration):
        winsound.Beep(2500, duration)


class Alerter(Logger, Beeper):
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
alerter = Alerter()

alerter.log("Wakey wakey!")
for i in range(30):
    alerter.beep(50)

msg = input("Enter an alert message: ")
alerter.doShortAlert(msg)

msg = input("Enter another alert message: ")
alerter.doMediumAlert(msg)

msg = input("And another: ")
alerter.doLongAlert(msg)