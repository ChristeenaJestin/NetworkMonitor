from scapy.all import sniff

from core.packet_parser import parse_packet

from database.db_manager import (
    initialize_database,
    insert_packet
)


def process_packet(packet):

    packet_data = parse_packet(packet)

    insert_packet(packet_data)


def start_sniffer():

    initialize_database()

    sniff(
        prn=process_packet,
        store=False
    )