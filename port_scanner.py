
# Port Scanner
# This script scans a range of ports on a specified IP address or domain name to check if they are open or closed.
# It uses threading to speed up the scanning process.
# It also includes error handling to manage socket connection issues.
# Import necessary libraries
import socket
import time
import threading

ascii_banner =  """
██████╗   ██████╗  ██████╗  ████████╗    ███████╗  ██████╗  █████╗  ███╗   ██╗ ███╗   ██╗ ███████╗ ██████╗ 
██╔══██╗ ██╔═══██╗ ██╔══██╗ ╚══██╔══╝    ██╔════╝ ██╔════╝ ██╔══██╗ ████╗  ██║ ████╗  ██║ ██╔════╝ ██╔══██╗
██████╔╝ ██║   ██║ ██████╔╝    ██║       ███████╗ ██║      ███████║ ██╔██╗ ██║ ██╔██╗ ██║ █████╗   ██████╔╝
██╔═══╝  ██║   ██║ ██╔══██╗    ██║       ╚════██║ ██║      ██╔══██║ ██║╚██╗██║ ██║╚██╗██║ ██╔══╝   ██╔══██╗
██║      ╚██████╔╝ ██║  ██║    ██║       ███████║ ╚██████╗ ██║  ██║ ██║ ╚████║ ██║ ╚████║ ███████╗ ██║  ██║
╚═╝       ╚═════╝  ╚═╝  ╚═╝    ╚═╝       ╚══════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═╝  ╚═══╝ ╚══════╝ ╚═╝  ╚═╝
    """
print(ascii_banner)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("Enter the target IP address or domain name: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))
print("-"*50)
print("scanning target: " + target) 
scan_time = time.time()
formatted_time = time.strftime("%H:%M:%S", time.localtime(scan_time))
print("Scan started at: " + formatted_time)
print("-"*50)

start = time.time()
print(f"Scanning {target} from port {start_port} to {end_port}...\n")

def scan_ports(ip, port_list):
    threads = []
    for port in port_list:
        thread = threading.Thread(target=start_port , args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
for port in range( start_port, end_port + 1):
    try:
        socket.connect((target, port))
        print(f"port {port} is open")
    except:
        print(f"port {port} is closed")
    finally:
        socket.close()

end = time.time()
print(f"Time taken {end - start:.2f} seconds")
