
import os
import time

from pathlib import Path
home = str(Path.home())

def writeSSLBypassSteam():  # Add SSL Bypass

    print("Installing SSL Bypass...")
    time.sleep(2)

    with open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\WindowsNoEditor\Engine.ini",'a') as mainfile:

        mainfile.write("\n[/Script/Engine.NetworkSettings]\nn.VerifyPeer=False")
    
    print("SSL Bypass has been Installed")
    os.system('pause')
    return

writeSSLBypassSteam()