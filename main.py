import socket
from host_discovery import *


def main():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind((localhost(), 6969))
    print(localhost())
    listener.listen()

if __name__ == '__main__':
    main()