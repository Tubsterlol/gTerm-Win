from pathlib import Path

ASCII_DIR = Path(__file__).parent.parent / "ascii"


def load_banner(name: str) -> str:
    path = ASCII_DIR / f"{name}.txt"
    return path.read_text()
