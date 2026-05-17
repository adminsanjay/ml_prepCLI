from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box
console=Console()
class DataDescription:
    tasks={
        "1":"Describe Specific Column",
        "2":"Show Dataset Properties",
        "3":"Show Dataset",
        "-1":"Back"
    }
    def __init__(self,data):
        self.data=data

    def show_columns(self):
        table=Table(title="Columns",box=box.ROUNDED,border_style="cyan")
        table.add_column("Column Names",style="bold green")
        for col in self.data.columns:
            table.add_row(col)
        console.print(table)

    def show_dataset(self):
        while True:
            try:
                rows=int(Prompt.ask("[bold cyan]Number of rows to display (-1 to go back)[/bold cyan]"))
                if rows==-1:
                    return self.data
                if rows<=0:
                    console.print("[bold red]Invalid Choice[/bold red]")
                    continue
                table=Table(title="Dataset Preview",box=box.MINIMAL_DOUBLE_HEAD,border_style="magenta")
                for col in self.data.columns:
                    table.add_column(str(col),style="cyan")
                for _,row in self.data.head(rows).iterrows():
                    table.add_row(*[str(x) for x in row.values])
                console.print(table)
                break
            except ValueError:
                console.print("[bold red]Integer Value Required[/bold red]")

    def describe_column(self):
        self.show_columns()
        while True:
            col=Prompt.ask("[bold cyan]Enter Column Name[/bold cyan]").lower()
            if col not in self.data.columns:
                console.print("[bold red]Column Not Found[/bold red]")
                continue
            console.print(Panel.fit(str(self.data[col].describe()),border_style="green"))
            break

    def dataset_properties(self):
        console.print(Panel.fit(str(self.data.describe()),title="Dataset Description",border_style="blue"))
        info_table=Table(title="Dataset Info",box=box.ROUNDED,border_style="yellow")
        info_table.add_column("Column",style="bold cyan")
        info_table.add_column("Datatype",style="bold green")
        info_table.add_column("NULL Values",style="bold red")
        for col in self.data.columns:
            info_table.add_row(str(col),str(self.data[col].dtype),str(self.data[col].isnull().sum()))
        console.print(info_table)

    def describe(self):
        while True:
            table=Table(title="Data Description Tasks",box=box.DOUBLE_EDGE,border_style="blue")
            table.add_column("Choice",style="bold yellow")
            table.add_column("Task",style="bold red")
            for key,value in self.tasks.items():
                table.add_row(key,value)
            console.print(table)
            choice=Prompt.ask("[bold cyan]Select Task[/bold cyan]")
            if choice=="1":
                self.describe_column()
            elif choice=="2":
                self.dataset_properties()
            elif choice=="3":
                self.show_dataset()
            elif choice=="-1":
                return self.data
            else:
                console.print("[bold red]Invalid Choice[/bold red]")
        return self.data