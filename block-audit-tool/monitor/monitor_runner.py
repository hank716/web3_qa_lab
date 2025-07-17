import time
import schedule
import subprocess

def run_compare():
    print("Running compare_data.py...")
    subprocess.run(["python", "scripts/compare_data.py"])

schedule.every(10).minutes.do(run_compare)

while True:
    schedule.run_pending()
    time.sleep(1)
