
import requests
import json
import time
import sys
import os

ENTRY_POINT = "http://maneevent.paperboat42.com/"
CODE_OK = 200
REFRESH_TIME = 5
DIR_NAME = "data"

def printData(value, isEnd=False):
    if isEnd:
        print(value, end="\r")
    else:
        print(value, end=" ")        
    sys.stdout.flush()

def waitingScreen():
    printData("Request Data")
    for _ in range(REFRESH_TIME - 1):
        time.sleep(1)
        printData(".")


if __name__ == "__main__":
    
    if not os.path.exists(DIR_NAME):
        os.makedirs(DIR_NAME)    

    while (True):

        os.system('cls')
        time.sleep(0.5)

        waitingScreen()

        r = requests.get(url = ENTRY_POINT)
        if r.status_code == 200:
            data = json.loads(r.text)
            for key in data.keys():
                name = key + ".txt"
                value = data[key]
                with open(DIR_NAME+ "/" + name, "w+") as f:
                    f.write(value)
            printData("DONE", True)

        else:
            printData("FAIL", True)

        time.sleep(0.5)
        

        
        
