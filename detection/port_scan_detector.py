import pandas as pd

PORT_SCAN_THRESHOLD = 20


def detect_port_scans():

    try:
        df = pd.read_csv("data/packet_logs.csv")

    except Exception:
        return []

    if df.empty:
        return []

    suspicious_ips = []

    grouped = df.groupby("src_ip")

    for ip, group in grouped:

        unique_ports = group["dst_port"].nunique()

        if unique_ports > PORT_SCAN_THRESHOLD:

            suspicious_ips.append({
                "source_ip": ip,
                "ports_scanned": int(unique_ports),
                "severity": "HIGH"
            })

    return suspicious_ips