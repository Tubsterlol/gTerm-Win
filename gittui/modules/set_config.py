import subprocess
from pathlib import Path
import questionary
from gittui.ascii_art import load_banner
from .utils import clear_terminal
from rich.console import Console

console = Console()


def get_git_config(scope_flag, key):
    try:
        result = subprocess.run(
            ["git", "config", scope_flag, "--get", key],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout.strip() or "(not set)"
    except Exception:
        return "(not set)"


def set_config():
    clear_terminal()
    console.print(load_banner("config_set"), style="bold magenta")

    scope = questionary.select(
        "Choose configuration scope:",
        choices=[
            "Global (applies to all repositories on this system)",
            "Local (applies only to this repository)",
        ],
    ).ask()

    if scope.startswith("Global"):
        scope_flag = "--global"
        cwd = Path.cwd()
    else:
        scope_flag = "--local"
        proj_dir = questionary.path("Enter the path to your project directory:").ask()
        cwd = Path(proj_dir).expanduser().resolve()
        if not cwd.exists():
            console.print(f"❌ Directory '{cwd}' does not exist.", style="bold red")
            return

    console.print("\nCurrent Git configuration:")
    console.print(f"User Name: {get_git_config(scope_flag, 'user.name')}")
    console.print(f"User Email: {get_git_config(scope_flag, 'user.email')}")
    console.print(f"Editor: {get_git_config(scope_flag, 'core.editor')}\n")

    username = questionary.text("Enter your Git username:").ask()
    email = questionary.text("Enter your Git email:").ask()

    editor = questionary.select(
        "Select your default text editor:",
        choices=["VSCode (default)", "Vim", "Nano", "Notepad", "Other"],
        default="VSCode (default)",
    ).ask()

    if editor == "VSCode (default)":
        editor_cmd = "code --wait"
    elif editor == "Vim":
        editor_cmd = "vim"
    elif editor == "Nano":
        editor_cmd = "nano"
    elif editor == "Notepad":
        editor_cmd = "notepad"
    else:
        editor_cmd = questionary.text("Enter custom editor command:").ask()

    try:
        subprocess.run(
            ["git", "config", scope_flag, "user.name", username], check=True, cwd=cwd
        )
        subprocess.run(
            ["git", "config", scope_flag, "user.email", email], check=True, cwd=cwd
        )
        subprocess.run(
            ["git", "config", scope_flag, "core.editor", editor_cmd],
            check=True,
            cwd=cwd,
        )

        console.print("\n✅ Git configuration saved successfully!", style="bold green")
        console.print(
            f"Scope: {scope_flag}\nUsername: {username}\nEmail: {email}\nEditor: {editor_cmd}",
            style="dim",
        )
    except subprocess.CalledProcessError:
        console.print("\n❌ Failed to apply Git configuration.", style="bold red")
