import json
import os
from pathlib import Path

def write_json_report(data, filename):
    Path(os.path.dirname(filename)).mkdir(parents=True, exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
