import random
import pandas as pd


def generate_confluence_kbs():
    kbs = [
        {
            "Title": f"KB Article {i + 1}",
            "Content": random.choice([
                "How to troubleshoot high CPU usage.",
                "Steps to optimize memory utilization.",
                "Guidelines to clean up disk space effectively.",
                "Techniques to improve network latency in distributed systems."
            ]),
            "Category": random.choice(["Troubleshooting", "Optimization", "General Knowledge", "Best Practices"]),
            "Difficulty Level": random.choice(["Beginner", "Intermediate", "Advanced"])
        } for i in range(50)  # Generate 50 KB articles
    ]
    pd.DataFrame(kbs).to_csv("confluence_kbs.csv", index=False)
    print("Generated Confluence dataset saved as 'confluence_kbs.csv'")


generate_confluence_kbs()
