def calculate_threat_score(alerts):

    score = 0

    for alert in alerts:

        severity = alert["severity"]

        if severity == "CRITICAL":

            score += 40

        elif severity == "HIGH":

            score += 20

        elif severity == "MEDIUM":

            score += 10

    return min(score, 100)