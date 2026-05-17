import pandas as pd
from rich.prompt import Prompt,Confirm
from rich.panel import Panel
from rich.console import Console
console=Console()
class Download:
    def __init__(self,data):
        self.data=data
    def download(self):
        filename=Prompt.ask("[bold cyan]Enter Filename (-1 to back)[/bold cyan]")
        if filename=="-1":
            return self.data
        if not filename.endswith(".csv"):
            filename+=".csv"
        try:
            self.data.to_csv(filename,index=False)
            console.print(Panel.fit(f"[bold green]{filename} Downloaded Successfully ✔[/bold green]",border_style="green"))
        except Exception as e:
            console.print(Panel.fit(f"[bold red]{e}[/bold red]",border_style="red"))
        if Confirm.ask("Exit Application?"):
            raise SystemExit
        return self.data