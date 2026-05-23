from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
import os

console = Console()

# Clear Terminal
os.system("cls" if os.name == "nt" else "clear")

# Logo / Banner
title = """
[bold cyan]
██╗      ██████╗  ██████╗ █████╗ ██╗     
██║     ██╔═══██╗██╔════╝██╔══██╗██║     
██║     ██║   ██║██║     ███████║██║     
██║     ██║   ██║██║     ██╔══██║██║     
███████╗╚██████╔╝╚██████╗██║  ██║███████╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝

██╗  ██╗ ██████╗ ███████╗████████╗███████╗██████╗ 
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
███████║██║   ██║███████╗   ██║   █████╗  ██████╔╝
██╔══██║██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝███████║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
[/bold cyan]

[bold white]                 HOSTFLOW v1.0[/bold white]
"""

console.print(Align.center(title))

# Server Information Table
info_table = Table(
    show_header=False,
    box=None,
    padding=(0, 3)
)

info_table.add_row(
    "[bold green]STATUS[/bold green]",
    "[white]ONLINE[/white]"
)

info_table.add_row(
    "[bold cyan]IP ADDRESS[/bold cyan]",
    "[white]192.168.XXX.XXX[/white]"
)

info_table.add_row(
    "[bold yellow]PORT[/bold yellow]",
    "[white]8080[/white]"
)

info_table.add_row(
    "[bold magenta]DIRECTORY[/bold magenta]",
    "[white]Downloads[/white]"
)

# Status Panel
status_panel = Panel(
    info_table,
    title="[bold white]SERVER STATUS[/bold white]",
    border_style="cyan",
    width=60,
    padding=(1, 2)
)

console.print(Align.center(status_panel))

# Menu Text
menu = """
[cyan][1][/cyan]  Start Server
[cyan][2][/cyan]  View Logs
[cyan][3][/cyan]  About

[red][0][/red]  Exit
"""

# Menu Panel
menu_panel = Panel(
    menu,
    title="[bold white]CONTROL PANEL[/bold white]",
    border_style="white",
    width=72,
    padding=(1, 2)
)

console.print(Align.center(menu_panel))

# Footer
footer = "[bold green]● READY[/bold green]   [white]HOSTFLOW is running smoothly[/white]"

console.print("\n")
console.print(Align.center(footer))
console.print("\n")