# generate_table.py
import pandas as pd
import os

data = [
    {"Name": "Alice", "Role": "Developer", "Status": "Active"},
    {"Name": "Bob", "Role": "Tester", "Status": "Inactive"},
    {"Name": "Charlie", "Role": "Manager", "Status": "Active"},
    {"Name": "Diana", "Role": "DevOps", "Status": "Active"},
]

df = pd.DataFrame(data)

# Generate styled HTML
styled_html = df.style.set_table_styles(
    [{'selector': 'th', 'props': [('background-color', '#f2f2f2'), ('text-align', 'center')]}]
).set_properties(**{'text-align': 'center'}).to_html()

html = f"""
<html>
<head>
    <title>Team Members</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
        }}
    </style>
</head>
<body>
    <h2>Team Members Table</h2>
    {styled_html}
</body>
</html>
"""

os.makedirs("output", exist_ok=True)
with open("output/index.html", "w") as f:
    f.write(html)
