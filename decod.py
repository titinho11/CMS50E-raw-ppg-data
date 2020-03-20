
import sys

#INPUT :
#    sys.argv[1] = the temp file where are recorded raw ppg data
#    sys.argv[2] = the final file where to output decoded ppg raw values  

#OUTPUT :
# nothing, just writtingg into sys.argv[2] file 

f = open(sys.argv[1], "r")
data = f.read()
f.close()
dataT = data.split('ffff') #in my device, it seem every 9 bytes data sent every second ended with theses value at the two last bytes
dataT.pop() #removing the last empty entry of the file 

count=0
ppgVal = []
for dat in dataT:
	print("New 7 bytes series : ",dat)
        byteTHex = [dat[i:i+2] for i in range(0 ,len(dat) ,2)]
        #print(byteTHex)
	    #octet = bin(int(myHex, 16))[2:].zfill(8)
        #dataBin = bin(int(dat,16))[2:].zfill(8)
        #print(dat, ' data Bin ', len(dataBin))
        #bytesBin = [dataBin[i:i+8] for i in range(0 ,len(dataBin) ,8)]
        #print (list(enumerate(bytesBin)))

        #first byte
	byte0 = bin(int(byteTHex[0], 16))[2:].zfill(8)
	
	#second byte (PPG Waveform data)
	byte1 = bin(int(byteTHex[3], 16))[2:].zfill(8) #this is the byte which get the ppg waveform value
	val = int(str(byte1)[:7],2) #ppg value is just the first 7 bits according to my ref (see repository readme)
	print(count,' 2nd byte ', byte1, ' => ', val) 
	ppgVal.append(val)
	count=count+1

#print(ppgVal)
f = open(sys.argv[2], "w") #writing in the output file the raw ppg data decoded, line by line
for l in ppgVal:
	f.write(str(l)+"\n") 
f.close()
