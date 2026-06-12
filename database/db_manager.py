import sqlite3

DB_FILE = "data/netsentry.db"


def get_connection():

    return sqlite3.connect(DB_FILE)


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS packets (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,

        src_ip TEXT,

        dst_ip TEXT,

        src_port INTEGER,

        dst_port INTEGER,

        protocol TEXT,

        packet_size INTEGER
    )
    """)

    conn.commit()

    conn.close()


def insert_packet(packet_data):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO packets (
        timestamp,
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        protocol,
        packet_size
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (

        str(packet_data["timestamp"]),

        packet_data["src_ip"],

        packet_data["dst_ip"],

        packet_data["src_port"],

        packet_data["dst_port"],

        packet_data["protocol"],

        packet_data["packet_size"]
    ))

    conn.commit()

    conn.close()