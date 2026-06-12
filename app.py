import streamlit as st

from streamlit_autorefresh import st_autorefresh

from core.traffic_analyzer import (
    get_total_packets,
    get_protocol_counts,
    get_top_ips,
    get_traffic_timeline,
    get_recent_packets
)

from dashboard.charts import (
    protocol_pie,
    top_ips_bar,
    traffic_timeline_chart
)

from detection.port_scan_detector import (
    detect_port_scans
)

from detection.icmp_flood_detector import (
    detect_icmp_flood
)

from detection.udp_flood_detector import (
    detect_udp_flood

)

from detection.anomaly_detector import (
    detect_anomalies
)

from detection.blacklist_checker import (
    check_blacklisted_ips
)

from detection.suspicious_ports import (
    detect_suspicious_ports
)

from detection.threat_score import (
    calculate_threat_score
)
# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------

st.set_page_config(
    page_title="NetSentry AI",
    page_icon="🛡️",
    layout="wide"
)

# ----------------------------------------
# LOAD CSS
# ----------------------------------------

with open("assets/styles.css") as css:

    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ----------------------------------------
# AUTO REFRESH
# ----------------------------------------

st_autorefresh(
    interval=2000,
    key="netsentry_refresh"
)

# ----------------------------------------
# LOAD DATA
# ----------------------------------------

total_packets = get_total_packets()

protocols = get_protocol_counts()

top_ips = get_top_ips()

traffic_timeline = get_traffic_timeline()

recent_packets = get_recent_packets()

# Existing Detectors

port_scan_alerts = detect_port_scans()

icmp_alerts = detect_icmp_flood()

udp_alerts = detect_udp_flood()

# Phase 4 Detectors

anomaly_alerts = detect_anomalies()

blacklist_alerts = check_blacklisted_ips()

port_alerts = detect_suspicious_ports()

# Combined Alerts

alerts = (

    port_scan_alerts

    + icmp_alerts

    + udp_alerts

    + anomaly_alerts

    + blacklist_alerts

    + port_alerts

)

# Threat Score

score = calculate_threat_score(
    alerts
)

# ----------------------------------------
# HEADER
# ----------------------------------------

st.markdown(
    """
# 🛡️ NetSentry AI

### Real-Time Network Monitoring &
### Intrusion Detection Platform
"""
)

st.divider()

# ----------------------------------------
# KPI CARDS
# ----------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📦 Total Packets",
        total_packets
    )

with col2:

    st.metric(
        "🌐 TCP",
        protocols.get("TCP", 0)
    )

with col3:

    st.metric(
        "📡 UDP",
        protocols.get("UDP", 0)
    )

with col4:

    st.metric(
        "⚠ ICMP",
        protocols.get("ICMP", 0)
    )

st.divider()

# ----------------------------------------
# CHARTS
# ----------------------------------------

left, right = st.columns(2)

with left:

    st.subheader(
        "📊 Protocol Distribution"
    )

    st.plotly_chart(
        protocol_pie(protocols),
        use_container_width=True
    )

with right:

    st.subheader(
        "🌍 Top Source IPs"
    )

    st.plotly_chart(
        top_ips_bar(top_ips),
        use_container_width=True
    )

# ----------------------------------------
# TRAFFIC TIMELINE
# ----------------------------------------

st.divider()

st.subheader(
    "📈 Network Traffic Timeline"
)

st.plotly_chart(
    traffic_timeline_chart(
        traffic_timeline
    ),
    use_container_width=True
)

# ----------------------------------------
# LIVE PACKET FEED
# ----------------------------------------

st.divider()

st.subheader(
    "📡 Live Packet Feed"
)

st.dataframe(
    recent_packets,
    use_container_width=True
)

# ----------------------------------------
# PROTOCOL STATS
# ----------------------------------------

st.divider()

st.subheader(
    "📋 Protocol Statistics"
)

st.json(protocols)
# ----------------------------------------
# THREAT SCORE
# ----------------------------------------

st.divider()

st.subheader(
    "🛡 Threat Score"
)

st.progress(
    score / 100
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Threat Score",
        f"{score}/100"
    )

with col2:

    st.metric(
        "Active Alerts",
        len(alerts)
    )

# ----------------------------------------
# SECURITY ALERTS
# ----------------------------------------

st.divider()

st.subheader(
    "🚨 Security Alerts"
)

if alerts:

    for alert in alerts:

        severity = alert.get(
            "severity",
            "LOW"
        )

        message = f"""
Type: {alert.get('type', 'Unknown')}

Source IP: {alert.get('source_ip', 'N/A')}

Count: {alert.get('packet_count', 0)}

Severity: {severity}
"""

        if severity == "CRITICAL":

            st.error(message)

        elif severity == "HIGH":

            st.warning(message)

        elif severity == "MEDIUM":

            st.info(message)

        else:

            st.info(message)

else:

    st.success(
        "No Security Alerts Detected"
    )