import sqlite3
import pandas as pd

DB_FILE = "data/netsentry.db"


def load_data():

    try:

        conn = sqlite3.connect(DB_FILE)

        df = pd.read_sql_query(
            "SELECT * FROM packets",
            conn
        )

        conn.close()

        return df

    except Exception:

        return pd.DataFrame()


def get_total_packets():

    df = load_data()

    return len(df)


def get_protocol_counts():

    df = load_data()

    if df.empty:
        return {}

    return (
        df["protocol"]
        .value_counts()
        .to_dict()
    )


def get_top_ips(limit=10):

    df = load_data()

    if df.empty:
        return {}

    return (
        df["src_ip"]
        .value_counts()
        .head(limit)
        .to_dict()
    )


def get_traffic_timeline():

    df = load_data()

    if df.empty:
        return pd.DataFrame()

    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    timeline = (
        df.groupby(
            pd.Grouper(
                key="timestamp",
                freq="10s"
            )
        )
        .size()
        .reset_index(name="packets")
    )

    return timeline


def get_recent_packets(limit=20):

    df = load_data()

    if df.empty:
        return pd.DataFrame()

    return df.tail(limit)


def get_unique_port_count():

    conn = sqlite3.connect(DB_FILE)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(DISTINCT dst_port)
        FROM packets
        """
    )

    result = cursor.fetchone()

    conn.close()

    if result and result[0]:
        return result[0]

    return 0