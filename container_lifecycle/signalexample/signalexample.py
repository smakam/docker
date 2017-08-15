#!/usr/bin/python

import sys
import signal
import time

def signal_handler_int(sigid, frame):
    print "signal", sigid, ",", "Handling Ctrl+C/SIGINT!"
    sys.exit(signal.SIGINT)

def signal_handler_term(sigid, frame):
    print "signal", sigid, ",", "Handling SIGTERM!"
    sys.exit(signal.SIGTERM)

def signal_handler_usr(sigid, frame):
    print "signal", sigid, ",", "Handling SIGUSR1!"
    sys.exit(0)

def main():
    # Register signal handler
    signal.signal(signal.SIGINT, signal_handler_int)
    signal.signal(signal.SIGTERM, signal_handler_term)
    signal.signal(signal.SIGUSR1, signal_handler_usr)

    while True:
        print "I am alive"
        sys.stdout.flush()
        time.sleep(1)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
