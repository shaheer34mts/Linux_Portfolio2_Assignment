This a an Assignment for "Linux for Embedded Objects" course in Robotics at SDU.

The main tasks of this assignments were:

1) Build a robot using Raspberry-Pi and CamJamEdu Robotics Kit than can follow the wall even if started a$
2) Set up a TCP server on port 8080 of Raspberry-Pi. This raspberry-pi should be able to get and execute $
3) Set up an adhoc network at Raspberry Pi

Setting up ad-hoc network at Raspberry-Pi:
1. first we saved our /etc/network/interfaces

cp /etc/network/interfaces /etc/network/interfaces.org

2. Then replaced the file with the following content

nano /etc/network/interfaces

auto wlan0
iface wlan0 inet static
     address 192.168.99.2
     netmask 255.255.255.0
     wireless-channel 1
     wireless-essid PiBott
     wireless-mode ad-hoc

3. After rebooting, ad-hoc network was visible and available to connect.



Setting up the TCP server:
We set up the TCP server on the robot's pi by writing a python script. Python has a built in library "socket" to setup socket communication.
We have to assign a Port number (8080 in this case) and an ip-address to which we want to connect (192.168.99.<groupnumber>).
Server was setup by using the command "socket.socket(socket.AF_INET, socket.SOCK_STREAM). This command defines what kind of connection do we want at our server (TCP/UDP in this case).
The server receives/sends data in the form of bytes only, so, in order to send command we have to encode/decde them into bytes. "utf-8" system was used to encode the messages. YOUR_CONNECTION.sendall(str.encode(YOUR_MESSAGE) command was used to do this task.
Buffer size defines the length of messages that are to be sent/received. The greater the buffer size, the highe the length of message that can be sent/received. YOUR_CONNECTION.recv(YOUR_BUFFER_SIZE) command is used to set the buffer size.
Once the server is set, we need to set our computer/other raspberry-pi as a client from where we can send our commands to the robot. We have to setup the socket connection in the way we did in the server script assign the ip-address and the port number. In order to decode the contents sent by server as a reply, we need to use YOUR_SERVER.recv(YOUR_BUUFER_SIZE) and YOUR_REPLY_FROM_SERVER.decode("Your encryption standard") (utf-8) in our case, commands.



Wall Following:
The robot is controlled via commands from the client. This is done with the commands:

	- "start" - will make the robot go straight forward.
	- "stop" - will make the robot stop.
	- "test" - will make the server write "Hello" back to the client
	- "getdist" - will make the robot reply with the distance output from the sensor in an interval between 0 and 100.
	- "followWall" - command will make the robot follow the wall if the robots startposition is at most slight angle to the wall. It run the followWall() in a preset amount of iterations.
	- "getmotors" - Command will give you the motorvalues of the robot
