import sys
import serial
import calendar;
import time;
import signal
import sys
import os
import threading

#INPUT :
#    sys.argv[1] = the serial port of CMS50E device
#    sys.argv[2] = the temp raw bytes data file where to output received bytes corresponding to real time ppg raw data  

#OUTPUT :
# nothing, just writtingg into sys.argv[2] file 


cmd_querry = b'\x7d\x81\xa1\x80\x80\x80\x80\x80\x80' #it seem that this is a request live data like command 

from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def signal_handler(sig, frame):
    tf = calendar.timegm(time.gmtime())
    print(tf-ts, ' Secondes recorded !')
    global rt
    global file
    rt.stop()
    with open(file, "a") as myfile:
        myfile.write(str(tf))
    sys.exit(0)

def maintain():
    #threading.Timer(54.0, maintain).start()
    serial.write(cmd_querry)

def delaistart():
    print("Start recording in...")
    print(5)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)


signal.signal(signal.SIGINT, signal_handler)
if os.path.exists(sys.argv[2]):
    os.remove(sys.argv[2])
serial = serial.Serial(sys.argv[1],
                                    baudrate=115200, #in my device, this is the baudrate where to open the serial, in other devices try 4800, 19200...
                                    timeout=2,
				    xonxoff=1,
				    bytesize=serial.EIGHTBITS,
				    stopbits=serial.STOPBITS_ONE,
                                    parity=serial.PARITY_NONE) #another important looking like parameter, setting the parity to NONE
                                    
#serial.write(cmd_querry)) 
#temporiser avec compteur
delaistart()
maintain()
file = sys.argv[2]
rt = RepeatedTimer(54, maintain) #send cmd_maintain every 54sec to maintain the stream session
print("Recording...\n^C to stop.")

ts = calendar.timegm(time.gmtime()) #10 caracteres a echapper dans le decodage de data
with open(sys.argv[2], "a") as myfile:
        myfile.write(str(ts))
while True:
    data = serial.read(9) #read each byte
    print(data)
    with open(sys.argv[2], "a") as myfile:
        myfile.write(data.hex())
