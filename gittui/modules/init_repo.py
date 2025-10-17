import subprocess
from pathlib import Path
import questionary
from gittui.ascii_art import load_banner
from .utils import clear_terminal
from rich.console import Console
from rich.panel import Panel

console = Console()


def init_repo():
    clear_terminal()
    console.print(load_banner("init_repo"), style="bold magenta")

    # Select directory
    use_current = questionary.confirm(
        "Initialize repository in current directory?"
    ).ask()
    if use_current is None:
        console.print("[red]Cancelled by user[/red]")
        return

    if use_current:
        repo_path = Path.cwd()
    else:
        path_str = questionary.text("Enter the path for your repository:").ask()
        if not path_str:
            console.print("[red]Cancelled by user[/red]")
            return
        repo_path = Path(path_str).expanduser().resolve()
        if not repo_path.exists():
            console.print(f"[red]Error: Path '{repo_path}' does not exist[/red]")
            return

    console.print(f"Target directory: [cyan]{repo_path}[/cyan]\n")

    commands = []
    commands.append(("git init", "Initializes a local Git repository"))

    add_all = questionary.confirm("Add all files to initial commit?").ask()
    if add_all is None:
        console.print("[red]Cancelled by user[/red]")
        return
    if add_all:
        commands.append(("git add .", "Adds all files and directories to staging"))

    create_commit = questionary.confirm("Create initial commit?").ask()
    if create_commit is None:
        console.print("[red]Cancelled by user[/red]")
        return
    if create_commit:
        commit_msg = questionary.text(
            "Enter commit message:", default="Initial commit"
        ).ask()
        if not commit_msg:
            console.print("[red]Cancelled by user[/red]")
            return
        commands.append((f'git commit -m "{commit_msg}"', "Commits staged changes"))

    panel_content = "\n".join([f"{cmd} → {desc}" for cmd, desc in commands])
    console.print(
        Panel(panel_content, title="Commands that are going to run", expand=False)
    )

    run_commands = questionary.confirm("Run these commands?").ask()
    if run_commands is None or not run_commands:
        console.print("[yellow]Aborted by user[/yellow]")
        return

    for cmd, _ in commands:
        console.print(f"[green]Running:[/green] {cmd}")
        subprocess.run(cmd, shell=True, cwd=repo_path)

    console.print("[bold green]Repository initialized successfully![/bold green]\n")
