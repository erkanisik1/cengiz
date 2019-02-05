#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown speech-dispatcher:speech-dispatcher /var/lib/speech-dispatcher -R")
    os.system("/bin/chown speech-dispatcher:speech-dispatcher /run/speech-dispatcher -R")
    os.system("/bin/chown speech-dispatcher:speech-dispatcher /var/log/speech-dispatcher -R")
