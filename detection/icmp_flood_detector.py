import sqlite3
import pandas as pd

DB_FILE = "data/netsentry.db"


def detect_icmp_flood(threshold=50):

    try:

        conn = sqlite3.connect(DB_FILE)

        df = pd.read_sql_query(
            "SELECT * FROM packets",
            conn
        )

        conn.close()

        if df.empty:
            return []

        icmp_packets = df[
            df["protocol"] == "ICMP"
        ]

        counts = (
            icmp_packets["src_ip"]
            .value_counts()
        )

        alerts = []

        for ip, count in counts.items():

            if count > threshold:

                alerts.append({

                    "type": "ICMP Flood",

                    "source_ip": ip,

                    "packet_count": int(count),

                    "severity": "CRITICAL"

                })

        return alerts

    except Exception:

        return []