import pandas as pd
from data_description import DataDescription
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box
console=Console()
class FeatureScaling:
    tasks = {
        '1':"Perform Normalization(MinMax Scaler)",
        '2':"Perform Standardization(Standard Scaler)",
        '3':"Show the Dataset"
    }
    tasks_normalization = {
        '1':"Normalize a specific Column",
        '2':"Normalize the whole Dataset",
        '3':"Show the Dataset"
    }
    tasks_standardization = {
        '1':"Standardize a specific Column",
        '2':"Standardize the whole Dataset",
        '3':"Show the Dataset"
    }
    def __init__(self, data):
        self.data = data
    
    def normalization(self):
        while(1):
            table=Table(title="Normalization Tasks",box=box.ROUNDED,border_style="cyan",title_style="bold cyan")
            table.add_column("Choice",style="bold yellow")
            table.add_column("Task",style="bold red")
            for key,value in self.tasks_normalization.items():
                table.add_row(key,value)
            console.print(table)
            while(1):
                try:
                    ch=Prompt.ask("[bold cyan]What you want to do? (Press -1 to go back)[/bold cyan]")
                    ch = int(ch)
                except ValueError:
                    console.print("[bold red]Invalid input. Please enter a valid integer😡[/bold red]")
                    continue
                break
            if ch == -1:
                return self.data
            elif ch == 1:
                console.print(f"[bold yellow]{self.data.dtypes}[/bold yellow]")
                cols=Prompt.ask("[bold cyan]Enter column names to normalize[/bold cyan]").lower()
                if cols=="-1":
                    return self.data
                for col in cols.split(" "):
                    try:
                        mx=self.data[col].max()
                        mn=self.data[col].min()
                        self.data[col]=(self.data[col]-mn)/(mx-mn)
                        console.print(f"[bold green]Column {col} normalized successfully[/bold green]")
                    except:
                        console.print(f"[bold red]Column {col} not found[/bold red]")
                console.print("[bold green]Normalization of a column completed successfully ✔[/bold green]")
            elif ch == 2:
                try:
                    self.data = pd.DataFrame(MinMaxScaler().fit_transform(self.data))
                    console.print("[bold green]Normalization on whole dataset completed successfully ✔[/bold green]")
                except:
                    console.print("[bold red]String Columns are present. So, NOT possible.[/bold red]")
            elif ch == 3:
                DataDescription(self.data).show_dataset()
            else:
                console.print("[bold red]Invalid choice[/bold red]")
        return self.data

    def standardization(self):
        while(1):
            table=Table(title="Standardization Tasks",box=box.ROUNDED,border_style="cyan",title_style="bold cyan")
            table.add_column("Choice",style="bold yellow")
            table.add_column("Task",style="bold red")
            for key,value in self.tasks_standardization.items():
                table.add_row(key,value)
            console.print(table)
            while(1):
                try:
                    ch=Prompt.ask("[bold cyan]What you want to do? (Press -1 to go back)[/bold cyan]")
                    ch = int(ch)
                except ValueError:
                    console.print("[bold red]Invalid input. Please enter a valid integer😡[/bold red]")
                    continue
                break
            if ch == -1:
                return self.data
            elif ch == 1:
                console.print(f"[bold yellow]{self.data.dtypes}[/bold yellow]")
                cols=Prompt.ask("[bold cyan]Enter column names to normalize[/bold cyan]").lower()
                if cols=="-1":
                    return self.data
                for col in cols.split(" "):
                    try:
                        mn=self.data[col].mean()
                        sd=self.data[col].std()
                        self.data[col]=(self.data[col]-mn)/(sd)
                        console.print(f"[bold green]Column {col} normalized successfully[/bold green]")
                    except:
                        console.print(f"[bold red]Column {col} not found[/bold red]")
                console.print("[bold green]Normalization of a column completed successfully ✔[/bold green]")
            elif ch == 2:
                try:
                    self.data = pd.DataFrame(StandardScaler().fit_transform(self.data))
                    console.print("[bold green]Normalization on whole dataset completed successfully ✔[/bold green]")
                except:
                    console.print("[bold red]String Columns are present. So, NOT possible.[/bold red]")
            elif ch == 3:
                DataDescription(self.data).show_dataset()
            else:
                console.print("[bold red]Invalid choice[/bold red]")
        return self.data
                
    def scaler(self):
        while(1):
            table=Table(title="Feature Scaling Tasks",box=box.ROUNDED,border_style="cyan",title_style="bold cyan")
            table.add_column("Choice",style="bold yellow")
            table.add_column("Task",style="bold red")
            for key,value in self.tasks.items():
                table.add_row(key,value)
            console.print(table)
            ch = Prompt.ask("[bold cyan]What you want to do? (Press -1 to go back)[/bold cyan]")
            if ch == "-1":
                return self.data
            elif ch == "1":
                self.normalization()
            elif ch == "2":
                self.standardization()
            elif ch == "3":
                DataDescription(self.data).show_dataset()
            else:
                console.print("[bold red]Invalid choice[/bold red]")
        return self.data