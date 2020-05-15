
import sys

#INPUT :
#    sys.argv[1] = the temp file where are recorded raw ppg data
#    sys.argv[2] = the final file where to output decoded ppg raw values  

#OUTPUT :
# nothing, just writtingg into sys.argv[2] file 

f = open(sys.argv[1], "r")
data = f.read()
f.close()

timestamp = data[:10] #retrieving timstamp
data = data[10:]
data = ''.join(data.split())[:-10]

print('Start Datetime : ', timestamp)

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
	   #second byte
	byte1 = bin(int(byteTHex[1], 16))[2:].zfill(8)
	#third byte
	byte2 = bin(int(byteTHex[2], 16))[2:].zfill(8)
	#fifth byte
	byte4 = bin(int(byteTHex[4], 16))[2:].zfill(8)
	#sixth byte
	byte5 = bin(int(byteTHex[5], 16))[2:].zfill(8)
	#seventh byte - 1:8 
	byte6 = bin(int(byteTHex[6], 16))[2:].zfill(8)
	val2 = int(str(byte6)[1:8],2) #SpO2 value seems to be the 0-6 bits of this byte


	#fourth byte (PPG Waveform data)
	byte3 = bin(int(byteTHex[3], 16))[2:].zfill(8) #this is the byte which get the ppg waveform value
	val = int(str(byte3)[:8],2) #ppg value seems to be the entire second byte
	#print(count,' 2nd byte ', byte3, ' => ', val) 
	ppgVal.append(str(val)+'-'+str(val2))
	count=count+1
	#print( str(byte4)[0:],'//', str(byte4)[1:],'//', str(byte4)[1:8],'//', str(byte4)[1:7],'//', str(byte4)[0:7]) #array[a:b], return element from the index a to the b-th element
	#print(int(str(byte0)[1:],2), '/', int(str(byte1)[1:],2), '/', int(str(byte2)[1:],2), '/', int(str(byte3)[0:],2), '/', int(str(byte4)[1:],2), '/', int(str(byte5)[1:],2), '/', int(str(byte6)[1:],2))
	

#print(ppgVal)
f = open(sys.argv[2], "w") #writing in the output file the raw ppg data decoded, line by line
f.write(timestamp+"\n") 
for l in ppgVal:
	f.write(str(l)+"\n") 
f.close()
