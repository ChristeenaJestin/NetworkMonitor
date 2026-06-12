# NetSentry AI

NetSentry AI is a real-time network monitoring and intrusion detection system developed using Python, Scapy, SQLite, Streamlit, and Machine Learning.

The project captures live network packets, analyzes traffic patterns, detects suspicious activities, and presents security insights through an interactive dashboard.

---

# Project Overview

The goal of NetSentry AI is to provide a lightweight security monitoring platform capable of:

- Capturing live network traffic
- Monitoring network activity in real time
- Detecting suspicious behavior
- Identifying common network attacks
- Generating security reports
- Applying machine learning for threat analysis

The system combines packet analysis, rule-based detection, and machine learning techniques to improve network visibility and security awareness.

---

# Features

### Network Monitoring

- Real-time packet capture using Scapy
- Traffic storage using SQLite
- Live packet feed dashboard
- Protocol monitoring (TCP, UDP, ICMP)

### Traffic Analytics

- Protocol distribution charts
- Top source IP analysis
- Network traffic timeline
- Packet statistics dashboard

### Threat Detection

- Port Scan Detection
- ICMP Flood Detection
- UDP Flood Detection
- Suspicious Port Monitoring
- Blacklisted IP Detection
- Traffic Anomaly Detection

### Threat Scoring

- Dynamic threat score calculation
- Active alert tracking
- Security risk visualization

### Machine Learning

- ML-based traffic classification
- Threat prediction model
- Automated threat assessment

### Reporting

- PDF security report generation
- Alert history export
- Historical threat tracking

---

# Architecture

```text
NetSentry AI
│
├── app.py
│
├── core/
│   ├── packet_sniffer.py
│   ├── packet_parser.py
│   └── traffic_analyzer.py
│
├── detection/
│   ├── port_scan_detector.py
│   ├── icmp_flood_detector.py
│   ├── udp_flood_detector.py
│   ├── anomaly_detector.py
│   ├── blacklist_checker.py
│   └── threat_score.py
│
├── dashboard/
│   ├── charts.py
│   ├── metrics.py
│   └── tables.py
│
├── ml/
│   ├── train_model.py
│   ├── threat_classifier.py
│   └── training_data.csv
│
├── ai/
│
├── reports/
│
├── data/
│
└── assets/
