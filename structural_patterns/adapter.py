import socket
import datetime


class SocketWriter(object):

    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET,
                                     socket.SOCK_DGRAM)
        self._ip = ip
        self._port = port

    def write(self, message):
        self._socket.send(message, (self._ip, self._port))


def log(message, destination):
    destination.write('[{}] - {}'.format(datetime.datetime.now(), message))


if __name__ == '__main__':
    udp_logger = SocketWriter('127.0.0.1', '9999')
    log('Something happened', udp_logger)