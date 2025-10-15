import datetime

gen = {
    "timeRelated" : ["time"],
    "dateRelated" : ["date"],
    "dayRelated" : ["day"],
}

class GEN:
    def __init__(self, word):
        self.word = word


    def showTime(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return "Current time is " + now + "is there any thing That I can help u sir ! "


    def checker(self, word):
        for i in gen:
            if word in gen[i]:
                pass
                












