
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=str, default="reports")
parser.add_argument("--db", type=str, default="chainwatcher.db")
args = parser.parse_args()
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_PATH = "chainwatcher.db"

def export_to_csv():
    conn = sqlite3.connect(args.db)
    df = pd.read_sql_query("SELECT * FROM block_data ORDER BY timestamp ASC", conn)
    conn.close()

    # export CSV
    os.makedirs("reports", exist_ok=True)
    csv_path = os.path.join(args.output_dir, "block_data.csv") + ""
    df.to_csv(csv_path, index=False)
    print(f"✅ export CSV to：{csv_path}")

    return df

def plot_block_trend(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["block_number"], label="Block Height", marker="o")
    plt.title("Block Height Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Block Height")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(args.output_dir, "block_trend.png") + "")
    print("✅ Block height chart saved to: reports/" + os.path.join(args.output_dir, "block_trend.png") + "")

def plot_latency(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["latency"], label="Latency (s)", color="orange", marker="x")
    plt.title("Latency Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Latency (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(args.output_dir, "latency_trend.png") + "")
    print("✅ Latency chart saved to: reports/" + os.path.join(args.output_dir, "latency_trend.png") + "")


if __name__ == "__main__":
    df = export_to_csv()
    plot_block_trend(df)
    plot_latency(df)
