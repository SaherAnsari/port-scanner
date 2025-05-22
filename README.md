# Port Scanner

A Python-based network port scanner that checks for open and closed ports on a specified target IP address or domain name.

## Description

This script scans a range of ports on a target host to determine which ports are open (accepting connections) and which are closed. It's designed to use threading for improved scanning performance, though the current implementation has some areas that could be optimized.

## Features

- Scan any IP address or domain name
- Customizable port range scanning
- Basic threading implementation for concurrent scanning
- Execution time measurement
- Simple command-line interface

## Requirements

- Python 3.x
- No external dependencies (uses only built-in libraries)

## Installation

1. Save the script as `port_scanner.py`
2. Ensure you have Python 3.x installed on your system

## Usage

Run the script from the command line:

```bash
python port_scanner.py
```

The script will prompt you for:
1. **Target IP address or domain name** (e.g., `192.168.1.1` or `example.com`)
2. **Start port** (e.g., `20`)
3. **End port** (e.g., `80`)

### Example

```
Enter the target IP address or domain name: 192.168.1.1
Enter the start port: 20
Enter the end port: 25
Scanning 192.168.1.1 from port 20 to 25...

port 20 is closed
port 21 is open
port 22 is open
port 23 is closed
port 24 is closed
port 25 is closed
Time taken 2.34 seconds
```

## Common Port Numbers

Some commonly scanned ports include:
- **21** - FTP
- **22** - SSH
- **23** - Telnet
- **25** - SMTP
- **53** - DNS
- **80** - HTTP
- **110** - POP3
- **143** - IMAP
- **443** - HTTPS
- **993** - IMAPS
- **995** - POP3S

## Important Warnings

⚠️ **Legal and Ethical Use Only**
- Only scan networks and systems you own or have explicit permission to test
- Unauthorized port scanning may be illegal in some jurisdictions
- Some networks may detect and block port scanning attempts
- Always respect terms of service and applicable laws

⚠️ **Network Considerations**
- Scanning large port ranges may generate significant network traffic
- Some firewalls and intrusion detection systems may flag port scanning as suspicious activity
- Be mindful of network resources when scanning

## Code Issues

**Note**: The current implementation has some technical issues that affect functionality:
1. Socket reuse problems that may cause connection errors
2. Threading implementation that doesn't properly distribute work
3. Exception handling that could be more specific

For production use, consider using established tools like `nmap` or implementing proper socket management and error handling.

## Performance Tips

- Smaller port ranges scan faster
- Local network targets typically respond faster than internet hosts
- Some hosts may have rate limiting that slows down rapid connection attempts

## Alternative Tools

For more advanced port scanning, consider:
- **Nmap** - Professional network discovery and security auditing
- **Masscan** - High-speed port scanner
- **Zmap** - Internet-wide network scanner

## Troubleshooting

**Connection timeouts**: Some hosts may not respond quickly; this is normal behavior.

**Permission errors**: On some systems, scanning certain ports may require elevated privileges.

**High port numbers**: Ports above 65535 don't exist; keep your range within 1-65535.

## License

This script is provided for educational and authorized testing purposes only. Use responsibly and in compliance with all applicable laws and regulations.

## Disclaimer

This tool is intended for network administrators, security professionals, and educational purposes. The authors are not responsible for any misuse of this software. Always ensure you have proper authorization before scanning any network or system.
