from pathlib import Path
import questionary
from rich.console import Console
from rich.panel import Panel
from gittui.ascii_art import load_banner

console = Console()


def open_repo():
    console.print(load_banner("open_repo"), style="bold magenta")

    # Ask for repository path
    path_str = questionary.path("Enter the path of the existing repository:").ask()
    if not path_str:
        console.print("[red]Cancelled by user[/red]")
        return

    repo_path = Path(path_str).expanduser().resolve()

    # Check if it’s a git repository
    if not (repo_path / ".git").exists():
        console.print(f"[red]Error:[/] '{repo_path}' is not a Git repository")
        return

    console.print(
        Panel(f"[green]Repository opened at:[/] {repo_path}", title="Success")
    )

    # show status, recent commits, branch info, etc.
