# gTerm-Win — Terminal-Based Git Assistant for Windows

> 💡 Looking for the **Linux version**?
> Check out [gTerm](https://github.com/Tubsterlol/gTerm)

<div align="center">
<pre>
     _____                   
    |_   _|                  
  __ _| | ___ _ __ _ __ ___  
 / _` | |/ _ \ '__| '_ ` _ \ 
| (_| | |  __/ |  | | | | | |
 \__, \_/\___|_|  |_| |_| |_|
  __/ |                      
 |___/                        

┌─────────────────────────────────────────────────────────────┐
│                 A terminal-based Git utility.               │
└─────────────────────────────────────────────────────────────┘ 
</pre>

</div>

gTerm-Win is a professional, **open-source** terminal user interface (TUI) for Git, designed to make version control intuitive, fast, and accessible from any Windows terminal (PowerShell or CMD). Inspired by tools like btop, gTerm-Win offers a menu-driven experience for everyday Git operations, eliminating the need to memorize complex commands.

---

## Overview

gTerm-Win simplifies Git workflows with an interactive interface built using [questionary](https://pypi.org/project/questionary/) and [rich](https://pypi.org/project/rich/). It is designed exclusively for Windows and is suitable for both beginners and advanced users.

Key features include:

* **Modular architecture**: Each Git operation is implemented in a dedicated Python module (e.g., `clone_repo.py`, `branch_manager.py`, `commit_existing_repo.py`, `commit_history.py`, `config_set.py`).
* **Utility modules**: `utils.py` for terminal clearing and `ascii_art.py` for displaying ASCII banners.
* **Interactive, menu-driven interface** for all major Git tasks.
* **Two release versions**: a precompiled non-editable binary and a fully open-source version for customization.

---

## Features

* Clone repositories interactively
* Initialize new repositories
* Open and inspect existing repositories
* Branch management: create, switch, delete, and list branches
* Commit changes with guided prompts
* View commit history in a readable format
* Configure Git settings (user name, email, profiles)
* Stash and restore work (WIP)
* Remote management (WIP)
* Status dashboard (WIP)
* Built-in help/manual
* Terminal cleaning after every action for a smooth TUI experience

---

## Installation on Windows (PowerShell)

1. **Install Python and Git**:
   Make sure Python 3.11+ and Git are installed and added to your PATH.

2. **Clone the repository**:

```powershell
git clone https://github.com/Tubsterlol/gTerm-Win.git
cd gTerm-Win
```

3. **Install dependencies**:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. **Add Python Scripts folder to PATH** (if not already):

```powershell
setx PATH "$env:PATH;C:\Users\<YourUsername>\AppData\Roaming\Python\Python311\Scripts"
```

5. **Run gTerm**:

```powershell
gterm
```

---

## Usage

gTerm-Win provides a menu-driven interface for all major Git operations. Simply type `gterm` and follow the prompts.

### Main Menu Options

* Initialize New Repository
* Clone Repository
* Open Existing Repository
* Recent Repositories
* Branch Manager
* Commit History Viewer
* Stash Manager (WIP)
* Remote Manager (WIP)
* Status Dashboard (WIP)
* Change Git Configuration (WIP)
* Switch Config Profile (WIP)
* gTerm Manual

---

## Development Philosophy

gTerm-Win is built to be:

* **Terminal-first**: No GUI dependencies, fast startup, native terminal feel
* **Modular**: Each Git operation is a separate Python file for easy extension
* **Open-source**: Transparent, hackable, community-driven
* **Windows-only**: Designed and tested exclusively for Windows 11+
* **Intuitive**: Suitable for learning and productivity

Two versions available:

* **Precompiled release**: Ready-to-run binary (non-editable) *(WIP)*
* **Open-source version**: For modification, extension, or contribution

---

## License

gTerm-Win is released under the MIT License. See [LICENSE](LICENSE) for details.
