#!/usr/bin/python python3

# Dencode - An Base64 Encode/Decode Tool
# Made By: Anmol Shah
# url: https://github.com/Anmolshah170/dencode


# Imports
import os
#import socket
#import subrocess
import sys
import time
#from datetime import datetime
import base64


def b64_encode():
    os.system('clear')
    message = input(">>> Enter the String to Encode: ")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("\n>>> Encoded String: ", base64_message)


def b64_decode():
    os.system('clear')
    base64message = input(">>> Enter the Encoded String: ")
    base64bytes = base64message.encode('ascii')
    messagebytes = base64.b64decode(base64bytes)
    message = messagebytes.decode('ascii')
    print("\n>>> Decoded String: ", message)


def main():
    os.system('clear')
    print("Welcome to dencode!")
    print("\nOptions:")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    choice = input("\nEnter You Choice: ")
    if choice == "1":
        b64_encode()
    elif choice == "2":
        b64_decode()
    elif choice == "3":
        print("\nByebye...")
        sys.exit()
    else:
        print("Wrong Input! Please Choose Wisely.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nexiting...")
        sys.exit()
