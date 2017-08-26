#!/usr/bin/env python3
#
# W. H. Bell
#
# A script to start the simple server
#

from SimpleServer import SimpleServer
import socket
import time

def main(argv=None):
  server = SimpleServer("127.0.0.1", 20000) # Create a simple server
  server.initialise() # Start the simple server.
  time.sleep(100) # Prevent the program from exiting

if __name__ == "__main__":
  main()
