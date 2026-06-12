from datetime import datetime

from scapy.layers.inet import (
    IP,
    TCP,
    UDP,
    ICMP
)


def parse_packet(packet):
    """
    Extract useful information from a packet.
    """

    packet_info = {
        "timestamp": datetime.now(),
        "src_ip": None,
        "dst_ip": None,
        "src_port": None,
        "dst_port": None,
        "protocol": "OTHER",
        "packet_size": len(packet)
    }

    # Check if packet contains IP layer
    if packet.haslayer(IP):

        packet_info["src_ip"] = packet[IP].src
        packet_info["dst_ip"] = packet[IP].dst

        # TCP
        if packet.haslayer(TCP):

            packet_info["protocol"] = "TCP"

            packet_info["src_port"] = packet[TCP].sport
            packet_info["dst_port"] = packet[TCP].dport

        # UDP
        elif packet.haslayer(UDP):

            packet_info["protocol"] = "UDP"

            packet_info["src_port"] = packet[UDP].sport
            packet_info["dst_port"] = packet[UDP].dport

        # ICMP
        elif packet.haslayer(ICMP):

            packet_info["protocol"] = "ICMP"

    return packet_info