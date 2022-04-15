import socket
import subprocess
import datetime
from timeit import default_timer as timer

# create a function to use the connect command for a given host
def port_scanner(target, port):
    s = socket.socket()
    try:
        s.connect((target, port))
    except:
        return False
    else:
        return True


# create a file with the scan results
filename = open("vi_scanner_results.txt", "w")

# Welcome page
print("\nWelcome to Port Scanner (V4.4)")
print("Vandelay Industries Copyright 2020")
print("=" * 50)

target = input("Please enter an IP to scan: ")


# user input for ports to scan
start_port = int(input("Enter starting port number: "))
end_port = int(input("Enter ending port number: "))
full_range = range(start_port, end_port+1, 1)

# breaking the page up with banner
print("=" * 50)

# make sure the "target" is up.
# if so start timer
# if not let the user know and exit the program
# remember to change this for windows
# code for mac and windows is different
# mac
status = subprocess.getstatusoutput(f"ping -c 1 {target}")
result = str(status)
if (result.startswith("(0")):
    print(f"\nHost: {target} is up. Scan beginning now.")
    # get the current time and print
    current_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    print(current_time)
    # write to the file
    response = ["Host:", target, "is up. Scan beginning now:", current_time, "\n"]
    response_out = ' '.join(response)
    filename.write(response_out)
   # start the timer
    start = timer()


else:
    print("Invalid IP. Goodbye.")
    response = ["IP:", target, "is invalid."]
    response_out = ' '.join(response)
    filename.write(response_out)
    exit()

# scan the ports and print results
for x in full_range:
    if port_scanner(target, x):
        print(f"Port {x} is open.")
        port_status = ["Port", str(x), "is open.\n"]
        port_status_out = ' '.join(port_status)
        filename.write(port_status_out)
    else:
        print(f"Port {x} is closed.")
        port_status = ["Port", str(x), "is closed.\n"]
        port_status_out = ' '.join(port_status)
        filename.write(port_status_out)

# the end of the scan
end = timer()

# add another banner to break up page
print("=" * 50)

# total time taken for scan
print("\nScan is complete.")
end_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
print(end_time)


# print(datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S'))

print(f"Total time for scan: {end-start:.2f} seconds.")

# write to file
fin_tup = ["Scan completed at", str(end_time), "\n", "Total time:", str(end-start)]
fin_out = ' '.join(fin_tup)
filename.write(fin_out)