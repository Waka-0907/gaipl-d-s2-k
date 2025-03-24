import pandas as pd

# Load datasets
def load_servicenow_data():
    return pd.read_csv("data/servicenow_incidents.csv")

def load_confluence_kbs():
    return pd.read_csv("data/confluence_kbs.csv")

def load_jira_issues():
    return pd.read_csv("data/jira_issues.csv")
