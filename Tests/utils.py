import csv
import re
from pathlib import Path
from typing import Any


def load_csv_data(filename: str) -> tuple[Any]:
    csv_filename = Path.cwd() / "test_data" / filename
    with open(csv_filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return [tuple(row) for row in reader]
    

def prettify_error_output(stderr: str) -> str:
    text = re.sub(r'\s+', ' ', stderr)
    return text.strip()