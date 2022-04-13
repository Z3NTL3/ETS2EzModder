import pyautogui
import os,sys
import asyncio, shutil
from pathlib import Path

# ETS2 Install All Mods At Once
ets2Location = "Documents\\Euro Truck Simulator 2"
class UnpackArchief(object):
    def __init__(self,archiveName,fileLocation,extractLocation):
        if shutil.unpack_archive(self.fileLocation,self.extractLocation):
            print(f"Unpacked {self.archiveName}")
        else:
            print(f"Could not unpack properly the archive: {self.archiveName}")
try:
    while True:
        gui = pyautogui.prompt(text="Enter folder name",title="Locate Folders",default=None)
        if gui == None:
            print("Please give us an folder name you want to load, if you wanna exit type exit")
        elif gui.lower() == "exit":
            sys.exit(0)
        else:
            if os.path.isdir(gui):
                break
            else:
                print("This folder does not exist, if you wanna exit type exit")
except:
    sys.exit(0)

async def Main(g = gui):
    HOMEDIR = Path.home()
    FILES = os.listdir(os.path.abspath(gui))
    FRESH_DIRS = []

    for file in files:
        if '.zip' in file or '.rar' in file:
            FRESH_DIRS.append(file)
        else:
            pass
    
    unpacked = 0
    for file in FRESH_DIRS:
        await asyncio.sleep(0)
        UnpackArchief(file, os.path.abspath(f"{gui}\\{file}"), HOMEDIR+ets2Location)
        unpacked += 1
    if unpacked < len(FRESH_DIRS):
        print("Some files were not properly installed")
    else:
        print("All files were correctly installed")
        
async def Startup():
    await asyncio.gather(
        Main()
    )

startLP = asyncio.new_event_loop()
startLP.run_until_complete(Startup())
