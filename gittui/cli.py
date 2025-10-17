#!/usr/bin/env python3

from gittui.ascii_art import load_banner
from gittui.prompts import ask_action
from .modules.init_repo import init_repo
from .modules.clone_repo import clone_repo
from rich.console import Console

console = Console()


def run():
    # Startup banner
    console.print(load_banner("welcome"), style="bold cyan")

    while True:
        choice = ask_action()

        if choice == "Quit" or choice is None:
            console.print("Goodbye! :(", style="bold green")
            break
        elif choice == "Initialize new repository":
            init_repo()
        elif choice == "Clone a repository":
            clone_repo()
            console.print(load_banner("clone_repo"), style="bold magenta")
        elif choice == "Open existing repository":
            console.print(load_banner("open_repo"), style="bold magenta")
        elif choice == "Git Configuration":
            console.print(load_banner("config"), style="bold magenta")
