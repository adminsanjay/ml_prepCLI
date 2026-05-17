from os import path
import pandas as pd
from rich.console import Console
from rich.panel import Panel
console=Console()
class DataInput:
    supported_file_extensions=[".csv"]
    def change_to_lower_case(self,data):
        data.columns=[col.lower() for col in data.columns]
        return data
   
    def get_data(self,file):
        filename,file_extension=path.splitext(file)
        if file_extension=="":
            console.print(Panel.fit("[bold red]Provide Dataset Name With Extension 🙃[/bold red]",border_style="red"))
            raise SystemExit
        if file_extension not in self.supported_file_extensions:
            console.print(Panel.fit("[bold red]Unsupported File Extension 🙃[/bold red]",border_style="red"))
            raise SystemExit
        try:
            data=pd.read_csv(filename+file_extension)
            console.print(Panel.fit("[bold yellow]Dataset File Is Ready ✔[/bold yellow]",border_style="yellow"))
        except pd.errors.EmptyDataError:
            console.print(Panel.fit("[bold red]Dataset File Is Empty 😵[/bold red]",border_style="red"))
            raise SystemExit
        except FileNotFoundError:
            console.print(Panel.fit("[bold red]File Doesn't Exist 😵[/bold red]",border_style="red"))
            raise SystemExit
        data=self.change_to_lower_case(data)
        return data