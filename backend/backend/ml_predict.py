import json
import joblib
import pandas as pd

def run():

    model = joblib.load("isolation_forest_model.pkl")
    encoders = joblib.load("feature_encoders.pkl")

    with open("drift_report.json","r") as f:
        drift_report = json.load(f)

    severity_map = {
        "NONE":0,
        "LOW":1,
        "MEDIUM":2,
        "HIGH":3,
        "CRITICAL":4
    }

    environment_map = {
        "development":0,
        "testing":1,
        "staging":2,
        "production":3
    }

    action_map = {
        "rollback":0,
        "modification":1
    }

    predictions=[]

    for event in drift_report:

        features = {
            "drift_detected": int(event["drift_detected"]),
            "severity": severity_map[event["severity"]],
            "environment": environment_map[event["environment"].lower()],
            "approval_status": encoders["approval_status"][event["approval_status"]],
            "maintenance_window": int(event["maintenance_window"]),
            "change_source": encoders["change_source"][event["change_source"]],
            "action": action_map[event["action"]],
            "domain": encoders["domain"][event["domain"]],
            "system": encoders["system"][event["system"]],
            "hour_of_day": pd.to_datetime(event["timestamp"]).hour
        }

        X = pd.DataFrame([features])

        prediction = model.predict(X)[0]
        score = float(model.decision_function(X)[0])

        predictions.append({

            "event_id": event["event_id"],

            "control_id": event["control_id"],

            "prediction": "Anomaly" if prediction == -1 else "Normal",

            "anomaly_score": round(score,4)

        })

    with open("ml_predictions.json","w") as f:
        json.dump(predictions,f,indent=4)

    print("\nML Prediction Completed")
    print("Total Records :",len(predictions))

    return "ml_predictions.json"

if __name__=="__main__":
    output=run()
    print(f"\nGenerated: {output}")