import json

class SYSTEM:
    SystemStatus = False
    warns = True

    def checkJson(self, fileName="keyWords.json"):
        fileCorrupt = False
        fileCheck = False

        with open("SystemChecks.json", "r+") as systemFile:
            systemData = json.load(systemFile)
            fileCheck = systemData["fileCheck"]
        if fileCheck:
            fileCorrupt = True

        try:
            with open("keyWords.json", "r+") as keywordFile:
                data = json.load(keywordFile)
        except Exception as e:
            return self.SystemStatus
        
        if fileCheck:
            for key in data:
                for value in data[key]:
                    for letters in value:
                        if letters.isupper():
                            fileCorrupt = True

        if fileCorrupt:
            normalForm = {}
            for key, val in data.items():
                sma = []
                for i in val:
                    sma.append(i.lower())
                normalForm[key] = sma
                sma = []
            
            with open(fileName, "w") as jsonFile:
                json.dump(normalForm, jsonFile, indent=4)

            systemData["fileCheck"] = True
            with open("SystemChecks.json", "w") as systemFile:
                json.dump(systemData, systemFile, indent=4)        
        return fileCheck



    def Status(self):
        if self.checkJson():
            self.SystemStatus = True


        return self.SystemStatus




