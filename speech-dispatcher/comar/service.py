# -*- coding: utf-8 -*-
import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "speech-dispatcher Daemon",
                 "tr": "speechd Servisi"})

@synchronized
def start():
    #if config.get("DAZUKO_SUPPORT", "no") == "yes":
    #            call("System.Service.start", "dazuko")

    startService(command="/usr/bin/speech-dispatcher -d",
            chuid="speech-dispatcher",
            pidfile="/run/speech-dispatcher/speech-dispatcher.pid",
            donotify=False)
    
    #if config.get("DAZUKO_SUPPORT", "no") == "yes":
    #    call("System.Service.stop", "dazuko")

def status():
    return isServiceRunning("/run/speech-dispatcher/speech-dispatcher.pid")
