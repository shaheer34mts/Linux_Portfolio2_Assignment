This a an Assignment for "Linux for Embedded Objects" course in Robotics at SDU.

The main tasks of this assignments were:

1) Build a robot using Raspberry-Pi and CamJamEdu Robotics Kit than can follow the wall even if started a$
2) Set up a TCP server on port 8080 of Raspberry-Pi. This raspberry-pi should be able to get and execute $
3) Set up an adhoc network at Raspberry Pi

Setting up ad-hoc network at Raspberry-Pi:






Setting up the TCP server:
We set up the TCP server on the robot's pi by writing a python script. Python has a built in library "soc$
We have to assign a Port number (8080 in this case) and an ip-address to which we want to connect (192.16$
Server was setup by using the command "socket.socket(socket.AF_INET, socket.SOCK_STREAM). This command de$
The server receives/sends data in the form of bytes only, so, in order to send command we have to encode/$
Buffer size defines the length of messages that are to be sent/received. The greater the buffer size, the$
Once the server is set, we need to set our computer/other raspberry-pi as a client from where we can send$
