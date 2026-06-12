from detection.port_scan_detector import detect_port_scans

alerts = detect_port_scans()

print("\nPort Scan Alerts\n")

for alert in alerts:
    print(alert)