import subprocess
import questionary
from rich.console import Console
from rich.panel import Panel
from gittui.ascii_art import load_banner
from .utils import clear_terminal

console = Console()


def commit_hist():
    clear_terminal()
    console.print(load_banner("commit_history"), style="bold magenta")

    while True:
        choice = questionary.select(
            "Select an option:",
            choices=["Detailed History", "Brief History", "Back"],
        ).ask()

        if choice in [None, "Back"]:
            break

        if choice == "Detailed History":
            cmd = ["git", "log", "--decorate", "--graph", "--all"]
        else:
            cmd = ["git", "log", "--oneline", "--graph", "--decorate"]

        try:
            result = subprocess.run(cmd, text=True, capture_output=True, check=False)
            if result.returncode != 0 or not result.stdout.strip():
                console.print(
                    Panel("No commits found or not a git repository.", style="red")
                )
            else:
                console.print(
                    Panel.fit(
                        result.stdout, title="Commit History", border_style="cyan"
                    )
                )
        except Exception as e:
            console.print(Panel(f"Error running git: {e}", style="bold red"))
