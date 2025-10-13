from pathlib import Path



path = Path(__file__).parent / "data"

with open(path / "quotes_cleaned.txt") as file:
    print(file.read())