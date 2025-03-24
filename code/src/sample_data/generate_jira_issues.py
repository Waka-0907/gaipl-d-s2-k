import random
import datetime
import pandas as pd

def generate_jira_issues():
    issues = [
        {
            "Issue Key": f"JIRA-{random.randint(1000, 9999)}",
            "Summary": random.choice([
                "Fix memory leak in service X.",
                "Optimize database queries for faster responses.",
                "Resolve server downtime issue.",
                "Enhance API to handle edge cases."
            ]),
            "Labels": random.choice(["Bug", "Improvement", "Task"]),
            "Status": random.choice(["Resolved", "In Progress", "To Do"]),
            "Timestamp": datetime.datetime.now() - datetime.timedelta(minutes=random.randint(0, 1440))
        } for _ in range(50)  # Generate 50 Jira issues
    ]
    pd.DataFrame(issues).to_csv("jira_issues.csv", index=False)
    print("Generated Jira dataset saved as 'jira_issues.csv'")


generate_jira_issues()
