import streamlit as st

from streamlit_autorefresh import st_autorefresh

from core.traffic_analyzer import (
    get_total_packets,
    get_protocol_counts,
    get_top_ips,
    get_traffic_timeline,
    get_recent_packets,
    get_unique_port_count
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

import pandas as pd

from reports.report_generator import (
    generate_pdf_report
)

from utils.alert_logger import (
    save_alerts
)

from ai.threat_explainer import (
    explain_alert
)

from ai.recommendation_engine import (
    recommend_action
)

from ml.threat_classifier import (
    classify_threat
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



traffic_timeline = get_traffic_timeline()

recent_packets = get_recent_packets()

total_packets = get_total_packets()

protocols = get_protocol_counts()

top_ips = get_top_ips()

unique_ports = get_unique_port_count()

ml_result = classify_threat(
    total_packets,
    unique_ports
)

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

save_alerts(alerts)

pdf_file = generate_pdf_report(
    alerts
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
# MACHINE LEARNING ANALYSIS
# ----------------------------------------

st.divider()

st.subheader(
    "🤖 Machine Learning Analysis"
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Unique Ports",
        unique_ports
    )

with col2:

    st.metric(
        "Packets Analysed",
        total_packets
    )

if ml_result["ml_threat"]:

    st.error(
        f"""
🚨 ML Threat Detected

Severity:
{ml_result['severity']}

Packet Count:
{total_packets}

Unique Ports:
{unique_ports}
"""
    )

else:

    st.success(
        """
✅ No ML Threat Detected

Traffic appears normal.
"""
    )


# ----------------------------------------
# REPORTS
# ----------------------------------------

st.divider()

st.subheader(
    "📄 Reports"
)

try:

    with open(
        pdf_file,
        "rb"
    ) as file:

        st.download_button(
            label="📥 Download PDF Report",
            data=file,
            file_name="security_report.pdf",
            mime="application/pdf"
        )

except:
    pass

try:

    with open(
        "data/alerts.csv",
        "rb"
    ) as file:

        st.download_button(
            label="📥 Download Alert History",
            data=file,
            file_name="alerts.csv",
            mime="text/csv"
        )

except:
    pass


# ----------------------------------------
# ALERT HISTORY
# ----------------------------------------

st.divider()

st.subheader(
    "📜 Alert History"
)

try:

    history = pd.read_csv(
        "data/alerts.csv"
    )

    st.dataframe(
        history.tail(50),
        use_container_width=True
    )

except:

    st.info(
        "No alert history available."
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

        analysis = explain_alert(
            alert
        )

        recommendation = (
            recommend_action(
                alert
            )
        )

        severity = alert.get(
            "severity",
            "LOW"
        )

        message = f"""
Type: {alert.get('type', 'Unknown')}

Source IP: {alert.get('source_ip', 'N/A')}

Packets: {alert.get('packet_count', 0)}

Severity: {severity}

AI Analysis:
{analysis}

Recommended Action:
{recommendation}
"""

        if severity == "CRITICAL":

            st.error(
                message
            )

        elif severity == "HIGH":

            st.warning(
                message
            )

        elif severity == "MEDIUM":

            st.info(
                message
            )

        else:

            st.success(
                message
            )

else:

    st.success(
        "No Security Alerts Detected"
    )