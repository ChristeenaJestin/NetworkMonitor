import joblib

model = joblib.load(
    "ml/netsentry_model.pkl"
)

def classify_threat(
    packet_count,
    unique_ports
):

    prediction = model.predict(
        [[
            packet_count,
            unique_ports
        ]]
    )[0]

    if prediction == 1:

        return {
            "ml_threat": True,
            "severity": "HIGH"
        }

    return {
        "ml_threat": False,
        "severity": "LOW"
    }