from serial import Serial, EIGHTBITS, STOPBITS_ONE
from serial.tools import list_ports
import time

class PyDuino(object):
    
    parameter = {'X': 0}
    
    @classmethod
    def scan(cls):
        ports = list_ports.comports()
        for port, desc, hwid in sorted(ports):
            print("{}: {} [{}]".format(port, desc, hwid))
        return ports
            
    def __init__(self, comport, baudrate=115200, timeout=20):
        self.controller = Serial(comport, baudrate=baudrate, bytesize=EIGHTBITS, stopbits = STOPBITS_ONE, timeout = timeout)
        time.sleep(1)
        print(self.controller.readline())
        
    def send_cmd(self, command, echo=True):
        if echo:
            print('input:', command)
        self.controller.write(command)
        time.sleep(.01)
        rtn = self.controller.readline().strip()
        if rtn != b'':
            print('ERR:' + str(rtn))
        else:   
            if echo:
                print(rtn)
        return str(rtn)
        
    def set_value(self, operation, param, value=0, echo=True):
        str_value = str(int(round(value)))
        command = ':'.join([operation + param, str_value+'\n']).encode()
        return self.send_cmd(command, echo)
    
    def close(self):
        self.controller.close()
    
def main():

    PyDuino.scan()
    aduino = PyDuino('COM7')
    
    rtn = aduino.set_value('C', 'X', 10000, echo=False)
    # print('serial rtn:', rtn)
    
    aduino.close()
    
if __name__ == '__main__':
    main()