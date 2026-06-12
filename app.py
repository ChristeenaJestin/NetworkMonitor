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

port_scan_alerts = detect_port_scans()

icmp_alerts = detect_icmp_flood()

udp_alerts = detect_udp_flood()

alerts = (
    port_scan_alerts
    + icmp_alerts
    + udp_alerts
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

        if severity == "CRITICAL":

            st.error(

                f"""
🚨 {alert['type']}

Source IP:
{alert['source_ip']}

Packets:
{alert['packet_count']}

Severity:
{severity}
"""
            )

        elif severity == "HIGH":

            st.warning(

                f"""
⚠ {alert['type']}

Source IP:
{alert['source_ip']}

Packets:
{alert['packet_count']}

Severity:
{severity}
"""
            )

        else:

            st.info(str(alert))

else:

    st.success(
        "No Security Alerts Detected"
    )