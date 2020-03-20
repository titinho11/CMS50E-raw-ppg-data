import sys
import serial

#INPUT :
#    sys.argv[1] = the serial port of CMS50E device
#    sys.argv[2] = the temp raw bytes data file where to output received bytes corresponding to real time ppg raw data  

#OUTPUT :
# nothing, just writtingg into sys.argv[2] file 

serial = serial.Serial(sys.argv[1],
                                    baudrate=115200, #in my device, this is the baudrate where to open the serial, in other devices try 4800, 19200...
                                    timeout=2,
				    xonxoff=1,
				    bytesize=serial.EIGHTBITS,
				    stopbits=serial.STOPBITS_ONE,
                                    parity=serial.PARITY_NONE) #another important looking like parameter, setting the parity to NONE
                                    
serial.write(b'\x7d\x81\xa1\x80\x80\x80\x80\x80\x80') #it seem that this is a request live data like command 
print("Recording...\n^C to stop.")
while True:
    data = serial.read() #read each byte
    with open(sys.argv[2], "a") as myfile:
        myfile.write(data.hex())
