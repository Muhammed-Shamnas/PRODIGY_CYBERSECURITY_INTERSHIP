from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if protocol == 6:
            proto = "TCP"
        elif protocol == 17:
            proto = "UDP"
        else:
            proto = "Other"

        print(f"Packet: {proto} {ip_src} -> {ip_dst}")

        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = packet[TCP].payload if packet.haslayer(TCP) else packet[UDP].payload
            print(f"Payload: {payload}")

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
