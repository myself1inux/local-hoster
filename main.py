from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from datetime import datetime
import socket
import os
import subprocess

console = Console()

server_process = None
logs = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_local_ip():

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.connect(("8.8.8.8", 80))

        ip = s.getsockname()[0]

        s.close()

        return ip

    except:

        return "127.0.0.1"


def add_log(message):

    current_time = datetime.now().strftime("%H:%M:%S")

    logs.append(
        f"[{current_time}] {message}"
    )

def start_server():
    global server_process

    if server_process is None:

        server_process = subprocess.Popen(
            ["python", "-m", "http.server", "8080"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        console.print("\n[bold green]SERVER STARTED[/bold green]")
        add_log("Server Started")
        ip = get_local_ip()
        console.print(f"[cyan]http://{ip}:8080[/cyan]\n")

    else:
        console.print("\n[yellow]Server already running.[/yellow]\n")


def stop_server():
    global server_process

    if server_process:

        server_process.terminate()
        server_process = None

        console.print("\n[bold red]SERVER STOPPED[/bold red]\n")
        add_log("Server Stopped")

    else:
        console.print("\n[yellow]No server is running.[/yellow]\n")


def view_logs():

    if logs:

        console.print("\n[bold cyan]SERVER LOGS[/bold cyan]\n")

        for log in logs:
            console.print(f"[white]{log}[/white]")

        console.print()

    else:
        console.print("\n[yellow]No logs available.[/yellow]\n")

def about():
    console.print("\n[bold cyan]HOSTFLOW v1.0[/bold cyan]")
    console.print("[white]Local Hosting Utility[/white]\n")


while True:

    clear()

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

    info_table = Table(
        show_header=False,
        box=None,
        padding=(0, 3)
    )

    status = "ONLINE" if server_process else "OFFLINE"

    info_table.add_row(
        "[bold green]STATUS[/bold green]",
        f"[white]{status}[/white]"
    )

    info_table.add_row(
        "[bold yellow]PORT[/bold yellow]",
        "[white]8080[/white]"
    )

info_table.add_row(
    "[bold cyan]IP ADDRESS[/bold cyan]",
    f"[white]{get_local_ip()}[/white]"
)

    status_panel = Panel(
        info_table,
        title="[bold white]SERVER STATUS[/bold white]",
        border_style="cyan",
        width=60,
        padding=(1, 2)
    )

    console.print(Align.center(status_panel))

    menu = """
[cyan][1][/cyan]  Start Server
[cyan][2][/cyan]  Stop Server
[cyan][3][/cyan]  View Logs
[cyan][4][/cyan]  About

[red][0][/red]  Exit
"""

    menu_panel = Panel(
        menu,
        title="[bold white]CONTROL PANEL[/bold white]",
        border_style="white",
        width=60,
        padding=(1, 2)
    )

    console.print(Align.center(menu_panel))

    console.print("\n")
    console.print(Align.center("[green]● READY[/green]"))

    choice = input("\nSelect Option > ")

    if choice == "1":
        start_server()

    elif choice == "2":
        stop_server()

    elif choice == "3":
        view_logs()

    elif choice == "4":
        about()

    elif choice == "0":

        if server_process:
            server_process.terminate()

        console.print("\n[red]Exiting HOSTFLOW...[/red]")
        break

    else:
        console.print("\n[red]Invalid option.[/red]")
        add_log("Invalid Option Selected")

    input("\nPress Enter to continue...")