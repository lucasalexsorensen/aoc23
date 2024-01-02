from pathlib import Path

import aocd  # type: ignore
import dotenv


def load_data(day: int, test=False) -> str:
    if test:
        return Path(f"test_data/d{day}.txt").read_text()
    dotenv.load_dotenv(override=True)
    return aocd.get_data(day=day, year=2023)
