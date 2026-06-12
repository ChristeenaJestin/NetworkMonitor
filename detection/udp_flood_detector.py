import sqlite3
import pandas as pd

DB_FILE = "data/netsentry.db"


def detect_udp_flood(threshold=100):

    try:

        conn = sqlite3.connect(DB_FILE)

        df = pd.read_sql_query(
            "SELECT * FROM packets",
            conn
        )

        conn.close()

        if df.empty:
            return []

        udp_packets = df[
            df["protocol"] == "UDP"
        ]

        counts = (
            udp_packets["src_ip"]
            .value_counts()
        )

        alerts = []

        for ip, count in counts.items():

            if count > threshold:

                alerts.append({

                    "type": "UDP Flood",

                    "source_ip": ip,

                    "packet_count": int(count),

                    "severity": "HIGH"

                })

        return alerts

    except Exception as e:

        print(
            f"UDP Flood Detection Error: {e}"
        )

        return []