from scapy.layers.inet import IP, TCP, UDP, ICMP


def parse_packet(packet):

    packet_info = {
        "src_ip": None,
        "dst_ip": None,
        "protocol": "OTHER",
        "packet_size": len(packet)
    }

    if packet.haslayer(IP):

        packet_info["src_ip"] = packet[IP].src
        packet_info["dst_ip"] = packet[IP].dst

        if packet.haslayer(TCP):
            packet_info["protocol"] = "TCP"

        elif packet.haslayer(UDP):
            packet_info["protocol"] = "UDP"

        elif packet.haslayer(ICMP):
            packet_info["protocol"] = "ICMP"

    return packet_info