#Author Raj
#This program will ping websites to see if they are down or up.
#This will be using sockets

#Import the the libray that is needed for the ping.
import subprocess
import socket as s 

host = "www.google.com"  #The website trying to ping 
ip = s.gethostbyname(host)


ping = subprocess.Popen( #Popen takes in 4 arguments as a function
    ["ping", "-w", "4", host], # The arguments will exute the ping command to the console
    stdout = subprocess.PIPE, # Will write the arguments to the console
    stderr = subprocess.PIPE  
)
out, error = ping.communicate()
print('The IP addrees of ' + host + ' is: ' + ip)
print(out)