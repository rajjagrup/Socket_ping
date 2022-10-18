#Author Raj
#This program will ping websites to see if they are down or up.
#This will be using sockets

#Import the the libray that is needed for the ping and for sockets.
import subprocess
import socket as s 

host = "www.google.com"  #The website trying to ping 
host_1 = "www.strose.edu"
ip = s.gethostbyname(host) #Stores the host "google.com" to the ip variable.
ip_1 = s.gethostbyname(host_1)#Stores the 
ping = subprocess.Popen( #Popen takes in 4 arguments as a function
    ["ping", "-w", "4", host], # The arguments will exute the ping command to the console
    stdout = subprocess.PIPE, # Will write the arguments to the console
    stderr = subprocess.PIPE  
)
out, error = ping.communicate()
out1 , error1 = ping.communicate()
print('The IP addrees of ' + host + ' is: ' + ip) #Will display the ip address of google.com
print('The IP addrees of ' + host_1 + ' is: ' + ip_1) #Will display the ip address of google.com
#print(out)