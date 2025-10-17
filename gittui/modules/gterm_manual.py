from rich.console import Console
from rich.panel import Panel
from gittui.ascii_art import load_banner
from .utils import clear_terminal

console = Console()


def gterm_manual():
    clear_terminal()
    console.print(load_banner("gterm_manual"), style="bold magenta")

    console.print(
        Panel(
            "[bold cyan]gTerm Manual[/bold cyan]\n\n"
            "[1] Initialize new repository → Create a new Git repo locally\n"
            "[2] Clone repository → Clone a remote repository\n"
            "[3] Open existing repository → Open a local repo for inspection\n"
            "───────────────────────────────────\n"
            "[4] Recent repositories → Quick access to recent repos\n"
            "[5] Branch manager → View or switch branches\n"
            "[6] Commit history viewer → View past commits\n"
            "[7] Stash manager → Manage stashes\n"
            "[8] Remote manager → Manage remotes\n"
            "[9] Status dashboard → View repo status\n"
            "───────────────────────────────────\n"
            "[10] Change git configuration → Set user.name/email\n"
            "[11] Switch config profile → Switch between saved git profiles\n"
            "[12] gTerm Manual → Show this help panel\n",
            title="gTerm Manual",
            expand=False,
        )
    )
