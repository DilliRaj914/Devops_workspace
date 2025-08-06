from flask import Flask, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def serve_table():
    # If file exists, serve it
    if os.path.exists("output/index.html"):
        return send_file("output/index.html")
    else:
        # Otherwise, regenerate
        data = [
            {"Name": "Alice", "Role": "Developer", "Status": "Active"},
            {"Name": "Bob", "Role": "Tester", "Status": "Inactive"},
            {"Name": "Charlie", "Role": "Manager", "Status": "Active"},
            {"Name": "Diana", "Role": "DevOps", "Status": "Active"},
        ]

        df = pd.DataFrame(data)

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

        return send_file("output/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
