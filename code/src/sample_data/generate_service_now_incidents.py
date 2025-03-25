import pandas as pd
import random
import datetime


def generate_servicenow_incidents():
    incidents = [
        {
            "Incident ID": f"INC{random.randint(1000, 9999)}",
            "Description": random.choice([
                "CPU usage exceeds threshold",
                "Memory leakage in application",
                "Disk space running low",
                "Service unavailable for users",
                "Network latency detected"
            ]),
            "Category": random.choice(["Performance", "Network", "Application", "Database"]),
            "Priority": random.choice(["Low", "Medium", "High", "Critical"]),
            "Impact Service": random.choice(["Web Server", "Database Server", "API Gateway", "Email Service"]),
            "Timestamp": datetime.datetime.now() - datetime.timedelta(minutes=random.randint(0, 1440))
        } for _ in range(100)  # Generate 100 sample incidents
    ]
    pd.DataFrame(incidents).to_csv("servicenow_incidents.csv", index=False)
    print("Generated ServiceNow dataset saved as 'servicenow_incidents.csv'")


generate_servicenow_incidents()
