# pyrefly: ignore [missing-import]
from termcolor import colored
# pyrefly: ignore [missing-import]
import click
# pyrefly: ignore [missing-import]
from rich.console import Console
# pyrefly: ignore [missing-import]
from rich.table import Table
# pyrefly: ignore [missing-import]
from rich.panel import Panel
# pyrefly: ignore [missing-import]
from rich.prompt import Prompt, Confirm
# pyrefly: ignore [missing-import]
from rich import box
from data_description import DataDescription
from data_input import DataInput
from imputation import Imputation
from download import Download
from categorical import Categorical
from feature_scaling import FeatureScaling

console=Console()

class Preprocessor:
    tasks={
        "1":"Data Description",
        "2":"Handle NULL Values",
        "3":"Encode Categorical Data",
        "4":"Feature Scaling",
        "5":"Download Modified Dataset",
        "6":"Show Dataset",
        "-1":"Exit"
    }

    def __init__(self):
        self.data=DataInput().get_data()
        console.print(Panel.fit("[bold green]Dataset Loaded Successfully 😁[/bold green]",border_style="green"))

    def show_columns(self):
        table=Table(title="Dataset Columns",box=box.ROUNDED,border_style="cyan")
        table.add_column("Index",style="bold yellow")
        table.add_column("Column Name",style="bold green")
        for idx,col in enumerate(self.data.columns):
            table.add_row(str(idx+1),col)
        console.print(table)

    def remove_column(self):
        self.show_columns()
        while True:
            col=Prompt.ask("[bold cyan]Enter column name to remove (-1 to skip)[/bold cyan]")
            if col=="-1":
                return
            if col not in self.data.columns:
                console.print("[bold red]Column not found[/bold red]")
                continue
            if Confirm.ask(f"Remove '{col}'?"):
                self.data.drop(columns=[col],inplace=True)
                console.print(f"[bold green]{col} removed successfully ✔[/bold green]")
                break

    def show_dataset(self):
        table=Table(title="Dataset Preview",box=box.MINIMAL_DOUBLE_HEAD,border_style="magenta")
        for col in self.data.columns:
            table.add_column(str(col),style="cyan")
        for _,row in self.data.head(10).iterrows():
            table.add_row(*[str(x) for x in row.values])
        console.print(table)

    def menu(self):
        table=Table(title="Preprocessing Tasks",box=box.DOUBLE_EDGE,border_style="blue")
        table.add_column("Choice",style="bold yellow")
        table.add_column("Task",style="bold green")
        for key,value in self.tasks.items():
            table.add_row(key,value)
        console.print(table)

    def run_task(self,choice):
        if choice=="1":
            DataDescription(self.data).describe()
        elif choice=="2":
            self.data=Imputation(self.data).imputer()
            console.print("[bold green]NULL handling completed ✔[/bold green]")
        elif choice=="3":
            self.data=Categorical(self.data).categoricalMain()
            console.print("[bold green]Encoding completed ✔[/bold green]")
        elif choice=="4":
            self.data=FeatureScaling(self.data).scaling()
            console.print("[bold green]Scaling completed ✔[/bold green]")
        elif choice=="5":
            Download(self.data).download()
            console.print("[bold green]Dataset downloaded ✔[/bold green]")
        elif choice=="6":
            self.show_dataset()
        elif choice=="-1":
            console.print(Panel.fit("[bold red]Exiting Preprocessor CLI 👋[/bold red]",border_style="red"))
            raise SystemExit
        else:
            console.print("[bold red]Invalid Choice[/bold red]")

    def main(self):
        self.remove_column()
        while True:
            self.menu()
            choice=Prompt.ask("[bold cyan]Select Task[/bold cyan]")
            self.run_task(choice)

@click.command()
def start():
    app=Preprocessor()
    app.main()

if __name__=="__main__":
    start()