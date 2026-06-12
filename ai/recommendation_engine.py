def recommend_action(alert):

    alert_type = alert.get(
        "type",
        ""
    )

    if alert_type == "Port Scan":

        return (
            "Block source IP and review "
            "firewall rules."
        )

    elif alert_type == "ICMP Flood":

        return (
            "Rate-limit ICMP traffic."
        )

    elif alert_type == "UDP Flood":

        return (
            "Enable UDP filtering and "
            "investigate source."
        )

    elif alert_type == "Traffic Anomaly":

        return (
            "Review traffic patterns and "
            "monitor source host."
        )

    elif alert_type == "Blacklisted IP":

        return (
            "Immediately block source IP."
        )

    return (
        "Further investigation required."
    )