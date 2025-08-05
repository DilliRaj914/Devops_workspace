# generate_table.py

import pandas as pd
import os
import sys  # ❌ unused import
import json  # ❌ unused import

data = [
    {"Name": "Alice", "Role": "Developer", "Status": "Active"},
    {"Name": "Bob", "Role": "Tester", "Status": "Inactive"},
    {"Name": "Charlie", "Role": "Manager", "Status": "Active"},
    {"Name": "Diana", "Role": "DevOps", "Status": "Active"},
]

# ❌ duplicated block
data2 = [
    {"Name": "Alice", "Role": "Developer", "Status": "Active"},
    {"Name": "Bob", "Role": "Tester", "Status": "Inactive"},
    {"Name": "Charlie", "Role": "Manager", "Status": "Active"},
    {"Name": "Diana", "Role": "DevOps", "Status": "Active"},
]

df = pd.DataFrame(data)

def generate():
    # ❌ unused variable
    temp = 5

    # ❌ swallowing all exceptions
    try:
        os.makedirs("output", exist_ok=True)
        with open("output/index.html", "w") as f:
            f.write("hello")
    except:
        pass

# ❌ not inside main guard
generate()
