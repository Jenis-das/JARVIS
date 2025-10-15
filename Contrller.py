import time
import json
import APIs

from Web.Search import SEARCH
from Auto.Iot import IOT
from Overall import GEN



class ControlMain:
    def __init__(self, word):
        self.word = word.lower()

    @staticmethod
    def control(*,className, word):
        obj = className(word)
        return obj.content()
        





# ---------------------------------------- Handle Modules ---------------------------------------- 
    def check(self):
        data = {}
        flag = False
        thatClass = ""
        content = ""


        try:
            with open("KeyWords.json") as keywords:
                data = json.load(keywords)
        except Exception as e:
            content = e


        for key in data:
            if self.word in data[key]:
                thatClass = key
                flag = True
                break


#  --------------------ALL Modules--------------------------
        MODULES = {
            "GEN": GEN,
            "IOT": IOT,
            "WEB": SEARCH,
            "APPS": "APPS"
        }

#  --------------------ALL Modules--------------------------



        thatClass = thatClass.upper()
        if thatClass in MODULES:
            content = self.control(className = MODULES[thatClass], word = self.word)
            

        return {"flag": flag, "content": content}





# ---------------------------------------- Handle Modules ---------------------------------------- 
    def historyHandler(self):
        pass

ob = ControlMain("SEARCH")
ob.check()