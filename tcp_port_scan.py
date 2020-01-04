import socket
from datetime import datetime

#Enter Host to Scan
host = input ("Enter Host Address or Target IP Address : ")
ip = socket.gethostbyname (host) #translate a hostname to ipv4 address format
portA = int(input("Enter Start Port to scan : "))
portB = int(input("Enter End Port to scan : "))
MaxPort = 65535

# if portA > MaxPort or portB > MaxPort:
#     print ("Nonexistant Port!")
#     break

#These three lines are cosmetic
print ("-" * 80)
print ("                 Please wait, Scanning the Host ---------------> ", ip)
print ("                 This will take some time          --------> ")
print ("-" * 80)
print ("-" * 80)

#starting time
t1 = datetime.now()

#Port scanning code
try: 
    for port in range (portA,portB + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #it creates a sock stream
        result = sock.connect_ex((ip,port))
        if result == 0:
            #if a socket is listening it will print out the port number
            print ("\n Port %d Is Open ---------------> " % (port))
            sock.close()
        else:
            print("\n Port %d is Closed =( " %(port))
except:
    print (f"Port {portA} and/or Port {portB} are out of range!")
    pass

#calculate end of exec time
t2 = datetime.now()
#calculate the difference
total = t2 - t1
#print the difference
print("Total Scanning Time : ", total)

print ("Press any key to exit")
x = input()
