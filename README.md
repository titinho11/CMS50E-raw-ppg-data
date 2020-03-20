# CONTEC PULSE OXIMETER CMS50E raw real time ppg Values
Raw ppg data from cms50e device
This repository allows you to record the raw live data from the cms50e and and save them in a file. You can edit it to plot these real time ppg values.


![Alt text](/cms50e.jpg "Contec Pulse Oximeter CMS50E")
*NB : There are apparently different versions of the cms50e. Not having found a code allowing me to retrieve the data from the version I had (above picture), I created this one. Moreover, the difference between the versions is often the serial opening baud and the real time raw data exchange protocol. With a little luck, you will find anyway other repository related to these versions;) .*

## Usage


Follow these instructions to retrieve raw real time data from the cms50e with this program.
1. Install python3 and the corresponding pip program
2. Install pyserial librarie by entering in a shell : `pip3 install pyserial`
3. Put your finger in the oximeter, turn it on, then plug into the PC. Make sure that it works well, i.e. that you can see the ppg curve vary on his screen before proceeding to the next step.
4. Run `cms50e.py` script passing to it as argument the port where the device is plug (in my example, the port is 'COM6') and the raw binary data output file (data in this case): `python3 cms50e.py COM6 data`. In Ubuntu, the command is something like `python3 cms50e.py \dev\ttyUSB0 data`
5. Press `^C` to stop the recording when you have enought data.
6. Run the script `decod.py` to convert theses raw data to ppg values into a file, from where you can read to operate on Matlab for example : `python3 decod.py data ppg.txt`. `data` is the ppg raw data output file and `ppg.txt` is the file which contains line by line ppg values. Now you can process this in Matlab or python to get the ppg curve.

Raw PPG from CMS50E (HR=63 on CMS50E).png
![Alt text](/ppg.png "Raw ppg curve from cms50e")

## Few remarks
- The code works both for Windows and Ubuntu
- The Sampling frequency of the device is 60Hz
- 60 time per second, the device send 9 bytes to the PC. The last two bytes seems to be always `ffff`, which i used as a delimitor
- the 4th byte contains, at his first 6 bits, the encoded raw ppg value
- To understand more about this protocol, please refers to : [Alex Robinson](https://www.tranzoa.net/~alex/blog/?p=371) and [Asbjørn Brask](https://www.atbrask.dk/?author=1)'s articles. It seems however that the encoding and protocol described by these articles are not always valid for my version of the CMS50e device. I stopped the investigation when the data I obtained was indeed a typical ppg curve, whose deduced Heart Rate value was moreover equal to the one displayed by the device.

## Debugging tricks
- About the 4fh step : if the device is not recognized, maybe [this driver](https://www.silabs.com/products/mcu/pages/usbtouartbridgevcpdrivers.aspx) is not installed in your PC. Check out on the internet if it is the case, and how to install that. But if you have the SPO2 Assistant software provided with the device installed in you PC, and if you can connect the device to that software, you should not have this issue. In Ubuntu, to make sure the device is well plug and recognized, enter `dmesg` in the terminal after plug in the device and look at the output. You should see something like the screen below :
![Alt text](https://www.atbrask.dk/wp-content/uploads/2015/03/dmesg.png "dmesg Output")
- About the 4fh step : under the conditions specified by step 2, the data recorded here correspond to the raw ppg values. On the other hand if you do not respect these conditions (finger out of the ppg...), this data will not correspond to the ppg value. Please refer to the above-mentioned documentation for more information.
- This code only retrieves information of interest without handling input or usage errors, please refer again to the above mentioned documentation to modify it or to make it more complete if necessary ;-)
