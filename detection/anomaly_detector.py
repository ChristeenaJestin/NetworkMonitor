import sqlite3
import pandas as pd

DB_FILE = "data/netsentry.db"


def detect_anomalies():

    try:

        conn = sqlite3.connect(DB_FILE)

        df = pd.read_sql_query(
            "SELECT * FROM packets",
            conn
        )

        conn.close()

        if df.empty:
            return []

        avg_size = df["packet_size"].mean()

        threshold = avg_size * 3

        suspicious = df[
            df["packet_size"] > threshold
        ]

        alerts = []

        for _, row in suspicious.iterrows():

            alerts.append({

                "type": "Traffic Anomaly",

                "source_ip": row["src_ip"],

                "packet_count": row["packet_size"],

                "severity": "MEDIUM"

            })

        return alerts

    except:

        return []