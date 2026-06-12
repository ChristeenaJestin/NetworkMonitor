import pandas as pd
import os

FILE = "data/alerts.csv"


def save_alerts(alerts):

    if not alerts:
        return

    df = pd.DataFrame(alerts)

    if os.path.exists(FILE):

        old = pd.read_csv(FILE)

        df = pd.concat(
            [old, df]
        )

    df.to_csv(
        FILE,
        index=False
    )