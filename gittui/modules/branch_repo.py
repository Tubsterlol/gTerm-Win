import subprocess
import questionary
from rich.console import Console
from rich.panel import Panel
from gittui.ascii_art import load_banner
from .utils import clear_terminal

console = Console()


def run_git_command(command, cwd=None):
    result = subprocess.run(
        command, shell=True, cwd=cwd, text=True, capture_output=True
    )
    if result.stdout:
        console.print(result.stdout.strip())
    if result.stderr:
        console.print(f"[red]{result.stderr.strip()}[/red]")


def branch_manager():
    clear_terminal()
    console.print(load_banner("branch_repo"), style="bold magenta")

    while True:
        choice = questionary.select(
            "Select branch operation (Run in working directory):",
            choices=[
                "List all branches",
                "Switch to branch",
                "Create new branch",
                "Delete a branch",
                "Rename a branch",
                "Back to main menu",
            ],
        ).ask()

        if choice == "Back to main menu" or choice is None:
            break

        if choice == "List all branches":
            result = subprocess.run(
                "git branch --all", shell=True, text=True, capture_output=True
            )
            branches = [b.strip() for b in result.stdout.splitlines() if b.strip()]
            branches = [b.replace("* ", "") for b in branches]
            if not branches:
                console.print("[red]No branches found.[/red]")
                continue

            console.print(
                Panel("\n".join(branches), title="All Branches", expand=False)
            )
            questionary.confirm("Press enter to continue").ask()

        # switch branch
        if choice == "Switch to branch":
            result = subprocess.run(
                "git branch --all", shell=True, text=True, capture_output=True
            )
            branches = [b.strip() for b in result.stdout.splitlines() if b.strip()]
            branches = [b.replace("* ", "") for b in branches]  # remove marker
            if not branches:
                console.print("[red]No branches found.[/red]")
                continue

            branch = questionary.select(
                "Select a branch to switch:", choices=branches
            ).ask()
            if branch:
                console.print(Panel(f"git switch {branch}", title="Command"))
                if questionary.confirm("Run this command?").ask():
                    run_git_command(f"git switch {branch}")

        # nwe branch
        elif choice == "Create new branch":
            branch_name = questionary.text("Enter new branch name:").ask()
            if branch_name:
                console.print(Panel(f"git checkout -b {branch_name}", title="Command"))
                if questionary.confirm("Run this command?").ask():
                    run_git_command(f"git checkout -b {branch_name}")

        # delete
        elif choice == "Delete a branch":
            result = subprocess.run(
                "git branch", shell=True, text=True, capture_output=True
            )
            branches = [
                b.strip().replace("* ", "")
                for b in result.stdout.splitlines()
                if b.strip()
            ]
            if not branches:
                console.print("[red]No local branches to delete.[/red]")
                continue

            branch = questionary.select(
                "Select a branch to delete:", choices=branches
            ).ask()
            if branch:
                console.print(Panel(f"git branch -d {branch}", title="Command"))
                if questionary.confirm("Run this command?").ask():
                    run_git_command(f"git branch -d {branch}")

        # renaem
        elif choice == "Rename a branch":
            old_branch = questionary.text("Enter the old branch name:").ask()
            new_branch = questionary.text("Enter the new branch name:").ask()
            if old_branch and new_branch:
                console.print(
                    Panel(f"git branch -m {old_branch} {new_branch}", title="Command")
                )
                if questionary.confirm("Run this command?").ask():
                    run_git_command(f"git branch -m {old_branch} {new_branch}")
