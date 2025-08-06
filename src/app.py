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

# Apply color styling
styled_df = df.style \
    .set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', '#4CAF50'), ('color', 'white'), ('text-align', 'center')]},
        {'selector': 'tbody td', 'props': [('text-align', 'center')]},
    ]) \
    .applymap(lambda x: 'color: red' if x == 'Inactive' else '', subset=["Status"]) \
    .set_properties(**{
        'border': '1px solid #ddd',
        'padding': '10px',
        'font-size': '16px'
    }) \
    .set_caption("🌟 <b>Stylish Team Table</b>")

# Wrap into full HTML
html = f"""
<html>
<head>
    <title>Team Members</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f9f9f9;
        }}
        h2 {{
            color: #333;
        }}
    </style>
</head>
<body>
    {styled_df.to_html()}
</body>
</html>
"""

# Save output
os.makedirs("output", exist_ok=True)
with open("output/index.html", "w") as f:
    f.write(html)
