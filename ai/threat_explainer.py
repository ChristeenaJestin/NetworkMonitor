def explain_alert(alert):

    alert_type = alert.get(
        "type",
        ""
    )

    if alert_type == "Port Scan":

        return (
            "Multiple ports were targeted "
            "from a single host. "
            "This may indicate "
            "reconnaissance activity."
        )

    elif alert_type == "ICMP Flood":

        return (
            "Large number of ICMP packets "
            "detected. Possible ping flood "
            "attack."
        )

    elif alert_type == "UDP Flood":

        return (
            "Large volume of UDP traffic "
            "detected. Possible DDoS "
            "activity."
        )

    elif alert_type == "Traffic Anomaly":

        return (
            "Traffic volume significantly "
            "higher than baseline. "
            "Requires investigation."
        )

    elif alert_type == "Blacklisted IP":

        return (
            "Traffic observed from a known "
            "malicious source."
        )

    else:

        return (
            "Unknown threat pattern."
        )