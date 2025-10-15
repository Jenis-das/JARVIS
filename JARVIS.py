from subprocess import run
from Sound.speak import speak
from Contrller import ControlMain
from System import SYSTEM


class JARVIS():
    def chat(self, InputTxt):
        reply = run(["ollama", "run", "gemma3:1b"],
            input=InputTxt.encode(),
            capture_output=True,
            check=True,
            text=False
            )
        

        return reply.stdout.decode().strip()
    
    def run(self):
        System = SYSTEM()
        Start = "new chat"
        while System.Status():
            JD = input("JD : ").lower().strip()
            ob = ControlMain(JD)
            obspeak = ob.check()      
            if obspeak["flag"]:
                print(obspeak["content"])
            elif JD == "exit":
                break
            elif JD == "new char" or Start == "new chat":
                Start = "old Chat"
                pass

            
            else:
                print(self.chat(JD))
            
ob = JARVIS()
ob.run()
