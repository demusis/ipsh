import time
import socket
from sense_hat import *
 

def get_ip_address():
    ip_address = '';
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


sh = SenseHat()
sh.clear()

sh.show_message('IP: %s' % get_ip_address(), text_colour=[50, 50, 50])
