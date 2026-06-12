# NetSentry AI

NetSentry AI is a network monitoring and intrusion detection dashboard built using Python.

The project captures live network packets, stores them in a SQLite database, analyzes traffic patterns, and displays the results through a Streamlit dashboard. It also includes basic threat detection features such as port scan detection, ICMP flood detection, and UDP flood detection.

## Features

* Live packet capture using Scapy
* Protocol analysis (TCP, UDP, ICMP)
* Source and destination IP monitoring
* Traffic statistics and visualizations
* Top source IP analysis
* Live packet feed
* Port scan detection
* ICMP flood detection
* UDP flood detection
* SQLite-based packet storage

## Technologies Used

* Python
* Scapy
* SQLite
* Pandas
* Plotly
* Streamlit

## Project Structure

NetworkMonitor/

├── core/               Packet capture and analysis

├── dashboard/          Dashboard visualizations

├── detection/          Threat detection modules

├── database/           Database utilities

├── reports/            Report generation

├── tests/              Testing scripts

├── utils/              Helper functions

├── app.py              Main Streamlit application

└── packet_capture_runner.py

## Running the Project

Install dependencies:

pip install -r requirements.txt

Start packet capture:

python packet_capture_runner.py

Launch dashboard:

streamlit run app.py

## Current Status

The current version supports packet capture, traffic analysis, dashboard visualization, and basic intrusion detection. Future work includes threat intelligence feeds, geographic IP visualization, anomaly detection, and automated report generation.

