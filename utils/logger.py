import csv
import os

LOG_FILE = "data/packet_logs.csv"


def initialize_log():

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "timestamp",
                "src_ip",
                "dst_ip",
                "src_port",
                "dst_port",
                "protocol",
                "packet_size"
            ])


def log_packet(packet_data):

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            packet_data["timestamp"],
            packet_data["src_ip"],
            packet_data["dst_ip"],
            packet_data["src_port"],
            packet_data["dst_port"],
            packet_data["protocol"],
            packet_data["packet_size"]
        ])