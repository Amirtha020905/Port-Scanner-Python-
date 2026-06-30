common_ports = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}
port = int(input("Enter Port Number: "))
if port in common_ports:
    print("Port Found")
    print("Service:", common_ports[port])
else:
    print("Unknown Port")
