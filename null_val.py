import pandas as pd
from data_description import DataDescription
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt ,Confirm
from rich.panel import Panel
from rich import box
class NullHandler:
    tasks = {
        "1":"Show NULL Values",
        "2":"Remove Columns",
        "3":"Fill NULL Values With Mean",
        "4":"Fill NULL Values With Median",
        "5":"Fill NULL Values With Mode",
        "6":"Show Dataset",
        "-1":"Back"
    }
    console=Console()
    def __init__(self,data):
        self.data=data
    
    def showColumns(self):
        table=Table(title="Columns",box=box.ROUNDED,header_style="bold blue")
        table.add_column("Column Names",style="bold green")
        for col in self.data.columns.values:
            table.add_row(col)
        self.console.print(table)
    
    def printNullValues(self):
        table=Table(title="NULL Values",box=box.ROUNDED,border_style="red")
        table.add_column("Column",style="bold cyan")
        table.add_column("NULL Count",style="bold yellow")
        for col in self.data.columns:
            table.add_row(col,str(self.data[col].isnull().sum()))
        self.console.print(table)
        return self.data
    
    def removeColumn(self):
        self.showColumns()
        while(1):
            col=Prompt.ask("Enter Column Names (space separated)").lower()
            if col=="-1":
                return self.data
            if Confirm.ask(f"Remove '{col}'?"):
                try:
                    self.data.drop(col.split(" "),axis=1,inplace=True)
                except KeyError:
                    self.console.print(Panel.fit("[bold red]Column Not Found ❌[/bold red]"))
                    continue
                self.console.print(Panel.fit("[bold green]Null Values Removed ✔[/bold green]"))
                break
            else:
                self.console.print(Panel.fit("[bold red]Not Deleting ❌[/bold red]"))
        return self.data
    
    def fillNullWithMean(self):
        self.showColumns()
        while(1):
            col=Prompt.ask("Enter Column Names (space separated)").lower()
            if col=="-1":
                return self.data
            if Confirm.ask(f"Remove '{col}'?"):
                try:
                    self.data[col] = self.data[col].fillna(self.data[col].mean())
                except KeyError:
                    self.console.print(Panel.fit("[bold red]Column Not Found ❌[/bold red]"))
                    continue
                except TypeError:
                    self.console.print(Panel.fit("[bold red]Not possible to fill Null Values with Mean ❌[/bold red]"))
                    continue
                self.console.print(Panel.fit("[bold green]Null Values Filled with Mean ✔[/bold green]"))
                break
            else:
                self.console.print(Panel.fit("[bold red]Not Changing ❌[/bold red]"))
        return self.data
    
    def fillNullWithMedian(self):
        self.showColumns()
        while(1):
            col=Prompt.ask("Enter Column Names (space separated)").lower()
            if col=="-1":
                return self.data
            if Confirm.ask(f"Remove '{col}'?"):
                try:
                    self.data[col] = self.data[col].fillna(self.data[col].median())
                except KeyError:
                    self.console.print(Panel.fit("[bold red]Column Not Found ❌[/bold red]"))
                    continue
                except TypeError:
                    self.console.print(Panel.fit("[bold red]Not possible to fill Null Values with Median ❌[/bold red]"))
                    continue
                self.console.print(Panel.fit("[bold green]Null Values Filled with Median ✔[/bold green]"))
                break
            else:
                self.console.print(Panel.fit("[bold red]Not Changing ❌[/bold red]"))
        return self.data
    
    def fillNullWithMode(self):
        self.showColumns()
        while(1):
            col=Prompt.ask("Enter Column Names (space separated)").lower()
            if col=="-1":
                return self.data
            if Confirm.ask(f"Remove '{col}'?"):
                try:
                    self.data[col] = self.data[col].fillna(self.data[col].mode()[0])
                except KeyError:
                    self.console.print(Panel.fit("[bold red]Column Not Found ❌[/bold red]"))
                    continue
                except TypeError:
                    self.console.print(Panel.fit("[bold red]Not possible to fill Null Values with Mode ❌[/bold red]"))
                    continue
                self.console.print(Panel.fit("[bold green]Null Values Filled with Mode ✔[/bold green]"))
                break
            else:
                self.console.print(Panel.fit("[bold red]Not Changing ❌[/bold red]"))
        return self.data

    def null_handler(self):
        while(1):
            table=Table(title="Null Value Handling Tasks",box=box.DOUBLE_EDGE,border_style="blue")
            table.add_column("Choice",style="bold yellow")
            table.add_column("Task",style="bold red")
            for key,value in self.tasks.items():
                table.add_row(key,value)
            self.console.print(table)
            choice=Prompt.ask("[bold cyan]Select Task[/bold cyan]")
            if choice=="1":
                self.printNullValues()
            elif choice=="2":
                self.removeColumn()
            elif choice=="3":
                self.fillNullWithMean()
            elif choice=="4":
                self.fillNullWithMedian()
            elif choice=="5":
                self.fillNullWithMode()
            elif choice=="6":
                DataDescription(self.data).show_dataset()
            elif choice=="-1":
                return self.data
            else:
                self.console.print("[bold red]Invalid Choice[/bold red]")
        return self.data