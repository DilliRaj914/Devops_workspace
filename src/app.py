# generate_table.py

import pandas as pd
import os
import sys  # 🟡 unused import (code smell)

data = [
    {"Name": "Alice", "Role": "Developer", "Status": "Active"},
    {"Name": "Bob", "Role": "Tester", "Status": "Inactive"},
    {"Name": "Charlie", "Role": "Manager", "Status": "Active"},
    {"Name": "Diana", "Role": "DevOps", "Status": "Active"},
]

df = pd.DataFrame(data)

# 🟡 Magic string duplication (code smell)
title = "Team Members"

def generate_table():
    # 🟡 Unused variable
    unused_value = 42

    # 🛑 Hardcoded file path (code smell)
    output_path = "output/index.html"

    # 🛑 Possible bug: HTML building without escaping inputs (low risk here, but bad practice)
    styled_html = df.style.set_table_styles(
        [{'selector': 'th', 'props': [('background-color', '#f2f2f2'), ('text-align', 'center')]}]
    ).set_properties(**{'text-align': 'center'}).to_html()

    html = f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <h2>{title} Table</h2>
        {styled_html}
    </body>
    </html>
    """

    try:
        os.makedirs("output", exist_ok=True)
        with open(output_path, "w") as f:
            f.write(html)
    except Exception as e:
        # 🛑 Bad practice: Swallowing all exceptions without logging
        pass

# 🛑 Dead code — not wrapped in main guard
generate_table()
