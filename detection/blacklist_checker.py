import sqlite3
import pandas as pd

DB_FILE = "data/netsentry.db"

BLACKLIST = [

    "1.1.1.1",

    "8.8.8.8",

    "45.33.32.156"

]


def check_blacklisted_ips():

    try:

        conn = sqlite3.connect(DB_FILE)

        df = pd.read_sql_query(
            "SELECT * FROM packets",
            conn
        )

        conn.close()

        alerts = []

        for ip in BLACKLIST:

            if ip in df["src_ip"].values:

                alerts.append({

                    "type": "Blacklisted IP",

                    "source_ip": ip,

                    "packet_count": 0,

                    "severity": "CRITICAL"

                })

        return alerts

    except:

        return []