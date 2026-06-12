import pandas as pd

from sklearn.ensemble import RandomForestClassifier

import joblib

data = pd.read_csv(
    "data/training_data.csv"
)

X = data[
    ["packet_count", "unique_ports"]
]

y = data[
    "is_anomaly"
]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(
    model,
    "ml/netsentry_model.pkl"
)

print("Model trained successfully")