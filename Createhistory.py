import History
import datetime
import os
import re




class HISTORY_CREATOR:

    def logs(self):
        CurrentTime = datetime.datetime.now().strftime("%I:%M:%S %p")
        TodayDate = datetime.date.today().strftime("%d-%m-%Y")
        TodaysDay = datetime.date.today().strftime("%A")
        insertLogs = "LOGS IN -> " + CurrentTime + " " + TodayDate + " " + TodaysDay + "\n"
        with open("History/LastVisit.txt", "+a") as file:
            file.write(insertLogs)

        return CurrentTime +"_"+ TodayDate +"_"+ TodaysDay
    
    def history(self):
        FileName = self.logs()
        FileName = re.sub(":","_",FileName)
        FileName = re.sub(" ","_",FileName)
        try:
            HistoryPath = "History/" + FileName + ".txt"
            with open(HistoryPath, "a+") as f:
                f.write("Time - ")
        except Exception as E:
            print(E)

    def run(self):
        self.history()


ob = HISTORY_CREATOR().run()