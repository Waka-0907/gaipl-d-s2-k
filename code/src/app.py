from flask import Flask, jsonify, request, render_template
from utils.dataset_loader import load_servicenow_data, load_confluence_kbs, load_jira_issues
from utils.llm import generate_recommendations

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/incidents")
def get_incidents():
    servicenow_data = load_servicenow_data()
    return servicenow_data.to_dict(orient="records")

@app.route("/kbs")
def get_kbs():
    confluence_kbs = load_confluence_kbs()
    return confluence_kbs.to_dict(orient="records")

@app.route("/issues")
def get_issues():
    jira_issues = load_jira_issues()
    return jira_issues.to_dict(orient="records")

@app.route("/recommendations", methods=["POST"])
def recommendations():
    data = request.json
    prompt = f"""
    Incident Details:
    - Incident ID: {data['incident_id']}
    - Description: {data['description']}
    - Category: {data['category']}
    - Resolution Comments: {data['resolution_comments']}
    - Change Record: {data['change_record']}

    Relevant Knowledge Base Articles:
    {data.get('kbs', 'None')}

    Relevant Historical Jira Issues:
    {data.get('issues', 'None')}

    Provide:
    1. Analysis of the situation.
    2. AI-driven recommendations.
    3. Optional follow-up actions requiring human approval.
    """
    recommendation = generate_recommendations(prompt)
    return jsonify({"recommendation": recommendation})

if __name__ == "__main__":
    app.run(debug=True)
