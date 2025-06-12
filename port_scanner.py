
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

target = input("Enter the target IP address or domain name: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

print("-"*50)
print("Scanning target: " + target)
scan_time = time.time()
formatted_time = time.strftime("%H:%M:%S", time.localtime(scan_time))
print("Scan started at: " + formatted_time)
print("-"*50)

start = time.time()
print(f"Scanning {target} from port {start_port} to {end_port}...\n")

# Function to scan individual port
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"[+] Port {port} is open")
    except:
        pass
    finally:
        s.close()

# Launch threads
threads = []
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(target, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()
print(f"\nScan complete. Time taken: {end - start:.2f} seconds")
