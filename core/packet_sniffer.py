from scapy.all import sniff
from core.packet_parser import parse_packet


def process_packet(packet):

    packet_data = parse_packet(packet)

    print(packet_data)


def start_sniffer():

    sniff(
        prn=process_packet,
        store=False
    )