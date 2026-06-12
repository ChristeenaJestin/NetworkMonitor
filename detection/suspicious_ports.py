import sqlite3
import pandas as pd

DB_FILE = "data/netsentry.db"

DANGEROUS_PORTS = [

    21,
    23,
    135,
    445,
    3389

]


def detect_suspicious_ports():

    try:

        conn = sqlite3.connect(DB_FILE)

        df = pd.read_sql_query(
            "SELECT * FROM packets",
            conn
        )

        conn.close()

        alerts = []

        for port in DANGEROUS_PORTS:

            hits = df[
                df["dst_port"] == port
            ]

            if len(hits) > 0:

                alerts.append({

                    "type": f"Suspicious Port {port}",

                    "source_ip":
                    hits.iloc[0]["src_ip"],

                    "packet_count":
                    len(hits),

                    "severity": "HIGH"

                })

        return alerts

    except:

        return []