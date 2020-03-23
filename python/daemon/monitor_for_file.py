#!/usr/bin/env python3

import time
from syspy import Shell
sh = Shell()

def run():
    while True:
        time.sleep(3) # sleep 3 seconds
        if sh.exists('./excel/file'):
            print('lit')
        else:
            print('not lit')

if __name__ == "__main__":
    run()
