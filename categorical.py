import pandas as pd
from data_description import DataDescription
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box
console=Console()
class Categorical:
    tasks = {
        '1' : "Show Categorical Columns",
        '2' : "Performing One Hot encoding",
        '3' : "Show the Dataset"
    }
    def __init__(self, data):
        self.data = data
    def categoricalColumn(self):
        table=Table(title="Unique columns in the dataset",box=box.ROUNDED,border_style="red")
        table.add_column("Categorical Column",style="bold cyan")
        table.add_column("Unique Values",style="bold yellow")
        for column in self.data.select_dtypes(include="object"):
            table.add_row(column,str(self.data[column].nunique()))
        console.print(table)
        return self.data
    def encoding(self):
        cat_cols=self.data.select_dtypes(include="object")
        while(1):
            col=Prompt.ask("[bold cyan]Enter column name to encode[/bold cyan]")
            if col=="-1":
                return self.data
            if col in cat_cols.columns:
                self.data=pd.get_dummies(data=self.data,columns=[col])
                console.print("[bold green]Encoding done[/bold green]")
                choice=Prompt.ask("[bold cyan]More columns to encode?(y/n)[/bold cyan]").lower()
                if choice=="y":
                    continue
                else:
                    self.categoricalColumn()
                    break
            else:
                console.print("[bold red]Column not found[/bold red]")
        return self.data      
    def categorical(self):
        while(1):
            table=Table(title="Categorical Encoding Tasks",box=box.DOUBLE_EDGE,border_style="blue")
            table.add_column("Choice",style="bold yellow")
            table.add_column("Task",style="bold red")
            for key,value in self.tasks.items():
                table.add_row(key,value)
            console.print(table)
            choice=Prompt.ask("[bold cyan]Select Task[/bold cyan]")
            if choice=="1":
                self.categoricalColumn()
            elif choice=="2":
                self.encoding()
            elif choice=="3":
                DataDescription(self.data).show_dataset()
            elif choice=="-1":
                return self.data
            else:
                console.print("[bold red]Invalid Choice[/bold red]") 
        return self.data