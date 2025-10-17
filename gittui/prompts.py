import questionary
from rich.console import Console
from rich.panel import Panel

from .modules.init_repo import init_repo as init_repo_util
from .modules.clone_repo import clone_repo as clone_repo_util
from .modules.open_repo import open_repo as open_repo_util
from .modules.branch_repo import branch_manager as branch_manager_util
from .modules.set_config import set_config as set_config_util
from .modules.commit_hist import commit_hist as commit_hist_util
from .modules.gterm_manual import gterm_manual
from .modules.utils import clear_terminal

console = Console()


def ask_action():
    while True:
        console.print(Panel("[bold magenta]gterm - Main Menu[/bold magenta]"))

        choice = questionary.select(
            "Select an option:",
            choices=[
                "────────────────────────────────────",
                "[1] Initialize new repository",
                "[2] Clone repository",
                "[3] Open existing repository",
                "────────────────────────────────────",
                "[4] Recent repositories",
                "[5] Branch manager",
                "[6] Commit history viewer",
                "[7] Stash manager",
                "[8] Remote manager",
                "[9] Status dashboard",
                "────────────────────────────────────",
                "[10] Change git configuration",
                "[11] Switch config profile",
                "[12] gTerm Manual",
                "────────────────────────────────────",
                "[Q] Quit gterm",
            ],
        ).ask()

        if choice is None or choice.startswith("[Q]"):
            break
        elif choice.startswith("[1]"):
            init_repo_util()
        elif choice.startswith("[2]"):
            clone_repo_util()
        elif choice.startswith("[3]"):
            open_repo_util()
        elif choice.startswith("[4]"):
            recent_repos_util()
        elif choice.startswith("[5]"):
            branch_manager_util()
        elif choice.startswith("[6]"):
            commit_hist_util()
        elif choice.startswith("[7]"):
            console.print("[yellow]Stash manager feature not implemented yet[/yellow]")
        elif choice.startswith("[8]"):
            console.print("[yellow]Remote manager not implemented yet[/yellow]")
        elif choice.startswith("[9]"):
            console.print("[yellow]Status dashboard not implemented yet[/yellow]")
        elif choice.startswith("[10]"):
            set_config_util()
        elif choice.startswith("[11]"):
            console.print(
                "[yellow]Switch config profile feature not implemented yet[/yellow]"
            )
        elif choice.startswith("[12]"):
            gterm_manual()
        elif choice.startswith("[Q]"):
            break
