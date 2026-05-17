import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from data_description import DataDescription
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
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
    def encoding(self):
        cat_cols=self.data.select_dtypes(include="object")
        while(1):
            col=Prompt.ask("[bold cyan]Enter column name to encode[/bold cyan]")
            if col=="-1":
                break
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
    def categorical(self):
        while(1):
            print("\nTasks\U0001F447")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required. Try again...\U0001F974")
                    continue
                break

            if choice == -1:
                break
            
            elif choice == 1:
                self.categoricalColumn()

            elif choice == 2:
                self.categoricalColumn()
                self.encoding()

            elif choice == 3:
                DataDescription.show_dataset(self)

            else:
                print("\nWrong Integer value!! Try again..\U0001F974")
        # return the data after modifying
        return self.data