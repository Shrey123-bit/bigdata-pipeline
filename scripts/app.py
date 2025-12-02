# scripts/app.py
import os
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

DATA_PATH = os.environ.get("DATA_PATH", "data/input.csv")

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/analytics")
def analytics():
    if not os.path.exists(DATA_PATH):
        return jsonify({"error": "input file not found", "path": DATA_PATH}), 404
    try:
        df = pd.read_csv(DATA_PATH)
        rows = len(df)
        columns = list(df.columns)
        summary = {
            "rows": rows,
            "columns": columns,
        }
        if rows > 0 and len(columns) > 0:
            top_values = df[columns[0]].value_counts().head(5).to_dict()
            summary["top_values_first_column"] = top_values
        return jsonify(summary), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
