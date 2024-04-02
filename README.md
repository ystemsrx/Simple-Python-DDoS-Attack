[中文版](README.zh.md)

# Simple-Python-DDoS-Attack


## Disclaimer
This script is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this script. Use it at your own risk.

## Overview
This Python script is designed to perform a DDOS attack by sending a large number of packets to a specified IP address or URL. It supports both UDP and TCP for sending packets. This tool is intended for learning and should not be used maliciously.

## Features
- Validate IP addresses.
- Convert URLs to IP addresses if a URL is provided.
- Send packets continuously to the targeted IP address or URL.

## Requirements
- Python 3.x
- Access to a terminal or command-line interface.

## How to Use
1. Make sure Python is installed on your system.
2. Open a terminal or command line.
3. Navigate to the directory containing the `ddos-attack.py` script.
4. Run the script using the following command:
   ```
   python ddos-attack.py
   ```
5. When prompted, enter the IP address or URL you wish to target.

## Note
- The script currently targets port 443 (HTTPS) and port 80 (HTTP) by default.
- Be aware of the legal implications of performing DDOS attacks. It is illegal to target networks or servers without permission.
